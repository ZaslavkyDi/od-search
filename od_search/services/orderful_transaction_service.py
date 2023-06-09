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
from od_search.services.api_handlers.orderful_api_handler import OrderfulApiHandler
from od_search.services.transaction_filters import (
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
    ) -> OrderfulTransactionTaskResponse:
        total_filtered_transactions: list[dict[str, Any]] = []
        last_transaction_page: int = self._calculate_last_transaction_page_number(
            number_checked_transactions=search_task.number_checked_transactions
        )

        for page in range(1, last_transaction_page + 1):
            pagination_query: PaginationQueryFilter = self._create_pagination_query(
                page_number=page
            )

            filtered_transactions: list[dict[str, Any]] = self._find_searched_transactions(
                pagination_query=pagination_query,
                transaction_task=search_task,
            )
            total_filtered_transactions.extend(filtered_transactions)

        multi_format_transactions_data: list[OrderfulTransactionTaskMultipleFormatItemResponse] = [
            self._extend_transaction_with_x12_format_if_exists(i)
            for i in total_filtered_transactions
        ]

        return OrderfulTransactionTaskResponse(
            metadata=search_task,
            total_items=len(multi_format_transactions_data),
            data=multi_format_transactions_data,
        )

    def _find_searched_transactions(
        self,
        pagination_query: PaginationQueryFilter,
        transaction_task: OrderfulTransactionTask,
    ) -> list[dict[str, Any]]:
        transactions_per_page: TransactionsResponse = self._api_handler.get_transactions(
            pagination=pagination_query,
            query_filter=transaction_task.transaction_query,
        )
        transaction_filter: BaseTransactionFilter = get_transaction_filter_by_name(
            name=transaction_task.searched_filter
        )
        searched_transaction = transaction_filter.filter(
            transaction_data=transactions_per_page.data,
            searched_text=transaction_task.searched_text,
        )

        return searched_transaction

    def _extend_transaction_with_x12_format_if_exists(
        self, transaction_json_data: dict[str, Any]
    ) -> OrderfulTransactionTaskMultipleFormatItemResponse:
        transaction_id: int = transaction_json_data["id"]

        x12_transaction_format: dict[str, Any] | None = None
        try:
            response_schema = self._api_handler.get_x12_transaction_format(
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
    def _calculate_last_transaction_page_number(number_checked_transactions: int) -> int:
        if number_checked_transactions < 1:
            raise ValueError(
                "The number of how many transaction need to check can not be less then 1."
            )

        page_number: float = (
            number_checked_transactions
            / get_orderful_settings().default_number_transaction_per_page
        )
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
