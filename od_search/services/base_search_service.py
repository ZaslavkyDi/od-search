import abc
import logging
import math
from typing import Any, Annotated, Protocol

from fastapi import Depends

from od_search.config import get_orderful_settings
from od_search.models.api_handler.orderful.response import (
    TransactionsResponse,
)
from od_search.models.pagination import PaginationQueryFilter
from od_search.models.requests import OrderfulTransactionTask
from od_search.models.responses import (
    OrderfulTransactionTaskResponse,
)
from od_search.common.orderful_api_handler import OrderfulApiHandler
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
