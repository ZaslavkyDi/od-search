import abc
import logging
import math
from typing import Any, Annotated, Protocol, AsyncGenerator

from fastapi import Depends

from od_search.config import get_orderful_settings
from od_search.models.api_handler.orderful.request import TransactionQueryFilter
from od_search.models.api_handler.orderful.response import (
    TransactionsResponse,
)
from od_search.models.pagination import PaginationQueryFilter
from od_search.models.requests import OrderfulTransactionTask
from od_search.models.responses import (
    OrderfulTransactionTaskResponse,
)
from od_search.common.orderful_api_handler import OrderfulApiHandler
from od_search.models.search_service import TransactionPageRange
from od_search.transaction_filters import (
    BaseTransactionFilter,
    get_transaction_filter_by_name,
)


logger = logging.getLogger(__name__)


class BaseSearchService(Protocol, metaclass=abc.ABCMeta):
    def __init__(
        self,
        api_handler: Annotated[OrderfulApiHandler, Depends(OrderfulApiHandler)],
    ) -> None:
        self._api_handler = api_handler

    @abc.abstractmethod
    async def search(self, search_task: OrderfulTransactionTask) -> OrderfulTransactionTaskResponse:
        pass

    async def _get_transactions_per_page_range(
        self,
        page_range: TransactionPageRange,
        transaction_query_filter: TransactionQueryFilter | None,
    ) -> AsyncGenerator[TransactionsResponse, None]:
        """
        Retrieves transactions for each page in the given page range.

        Args:
        page_range: The range of page numbers to retrieve transactions for.
        transaction_query_filter: Filters to apply to the transaction query.

        Yields:
        TransactionsResponse: The transactions for a given page.
        """
        for page in range(page_range.start_page_number, page_range.end_page_number + 1):
            pagination_query = self._create_pagination_query(page_number=page)
            transactions_per_page: TransactionsResponse = (
                await self._api_handler.get_json_transactions(
                    pagination=pagination_query,
                    query_filter=transaction_query_filter,
                )
            )
            yield transactions_per_page

    def _get_transactions_pages_range(
        self, search_task: OrderfulTransactionTask
    ) -> TransactionPageRange:
        first_transaction_page: int = self._calculate_first_transaction_page(
            number_transactions_offset=search_task.transactions_offset,
        )
        last_transaction_page: int = self._calculate_last_transaction_page_number(
            number_checked_transactions=search_task.transactions_for_check,
            number_transactions_offset=search_task.transactions_offset,
        )
        return TransactionPageRange(
            start_page_number=first_transaction_page,
            end_page_number=last_transaction_page,
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
