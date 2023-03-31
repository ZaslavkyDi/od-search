import json
import logging
import math
from typing import Any, Annotated

from fastapi import Depends

from od_search.config import get_orderful_settings
from od_search.models.api_handler.orderful.response import (
    TransactionsResponse,
)
from od_search.models.pagination import PaginationQueryFilter
from od_search.models.requests import OrderfulTransactionTask
from od_search.models.responses import (
    OrderfulTransactionTaskResponse,
    OrderfulTransactionTaskMultipleFormatItemResponse,
)
from od_search.common.orderful_api_handler import OrderfulApiHandler
from od_search.transaction_filters import (
    BaseTransactionFilter,
    get_transaction_filter_by_name,
)


logger = logging.getLogger(__name__)


class OrderfulTransactionService:
    def __init__(
        self,
        api_handler: Annotated[OrderfulApiHandler, Depends(OrderfulApiHandler)],
    ) -> None:
        self._api_handler = api_handler

    async def search(
        self,
        search_task: OrderfulTransactionTask,
        include_x12: bool = False,
    ) -> OrderfulTransactionTaskResponse:
        total_filtered_transactions: list[dict[str, Any]] = []
        first_transaction_page: int = self._calculate_first_transaction_page(
            number_transactions_offset=search_task.transactions_offset,
        )
        last_transaction_page: int = self._calculate_last_transaction_page_number(
            number_checked_transactions=search_task.transactions_for_check,
            number_transactions_offset=search_task.transactions_offset,
        )

        for page in range(first_transaction_page, last_transaction_page + 1):
            pagination_query: PaginationQueryFilter = self._create_pagination_query(
                page_number=page
            )
            transaction_per_page: TransactionsResponse = (
                await self._api_handler.get_json_transactions(
                    pagination=pagination_query,
                    query_filter=search_task.transaction_query,
                )
            )

            filtered_transactions: list[dict[str, Any]] = self._filter_transactions(
                transactions_response=transaction_per_page,
                transaction_task=search_task,
            )
            total_filtered_transactions.extend(filtered_transactions)

        multi_format_transactions_data: list[OrderfulTransactionTaskMultipleFormatItemResponse] = [
            await self._extend_transaction_with_x12_format_if_exists(i, include_x12)
            for i in total_filtered_transactions
        ]

        return OrderfulTransactionTaskResponse(
            metadata=search_task,
            total_items=len(multi_format_transactions_data),
            data=multi_format_transactions_data,
        )

    @staticmethod
    def _filter_transactions(
        transactions_response: TransactionsResponse,
        transaction_task: OrderfulTransactionTask,
    ) -> list[dict[str, Any]]:
        transaction_filter: BaseTransactionFilter = get_transaction_filter_by_name(
            name=transaction_task.searched_filter
        )
        searched_transaction = transaction_filter.filter(
            transaction_data=transactions_response.data,
            searched_text=transaction_task.searched_text,
        )

        return searched_transaction

    async def _extend_transaction_with_x12_format_if_exists(
        self,
        transaction_json_data: dict[str, Any],
        include_x12: bool = False,
    ) -> OrderfulTransactionTaskMultipleFormatItemResponse:
        transaction_id: int = transaction_json_data["id"]

        x12_transaction_format: dict[str, Any] | None = None
        if include_x12:
            try:
                response_schema = await self._api_handler.get_x12_transaction(
                    transaction_id=transaction_id
                )
                x12_transaction_format = json.loads(response_schema.json())
            except ValueError as e:
                logger.warning(str(e))

        return OrderfulTransactionTaskMultipleFormatItemResponse(
            json_format=transaction_json_data,
            x12_format=x12_transaction_format,
        )

    @staticmethod
    def _calculate_first_transaction_page(number_transactions_offset: int) -> int:
        page_number: float = (
            number_transactions_offset / get_orderful_settings().default_number_transaction_per_page
        )
        if page_number < 1:
            return 1

        return math.ceil(page_number)

    @staticmethod
    def _calculate_last_transaction_page_number(
        number_checked_transactions: int, number_transactions_offset: int = 0
    ) -> int:
        if number_checked_transactions < 1:
            raise ValueError(
                "The number of how many transaction need to check can not be less then 1."
            )

        page_number: float = (
            number_checked_transactions + number_transactions_offset
        ) / get_orderful_settings().default_number_transaction_per_page
        return math.ceil(page_number)

    @staticmethod
    def _create_pagination_query(page_number: int) -> PaginationQueryFilter:
        limit: int = get_orderful_settings().default_number_transaction_per_page
        total: int = page_number * limit
        offset: int = total - limit

        return PaginationQueryFilter(
            offset=offset,
            limit=limit,
            total=total,
        )
