import math
from typing import Any

from od_search.config import get_orderful_settings
from od_search.config.constants import TransactionFilterName
from od_search.models.api_handler.orderful.response import TransactionsResponse
from od_search.models.pagination import PaginationQueryFilter
from od_search.models.service_tasks import OrderfulTransactionTask
from od_search.services.api_handlers.orderful_api_handler import OrderfulApiHandler
from od_search.services.transaction_filters import (
    BaseTransactionFilter,
    get_transaction_filter_by_name,
)


class OrderfulTransactionService:
    def __init__(self, api_handler: OrderfulApiHandler) -> None:
        self._api_handler = api_handler

    def find_transactions_by_filter(
        self,
        filter_name: TransactionFilterName,
        transaction_task: OrderfulTransactionTask,
    ) -> list[dict[str, Any]]:
        total_filtered_transactions: list[dict[str, Any]] = []
        last_transaction_page = self._calculate_last_transaction_page_number(
            number_checked_transactions=transaction_task.number_checked_transactions
        )

        for page in range(1, last_transaction_page + 1):
            pagination_query = self._create_pagination_query(page_number=page)

            filtered_transactions = self._find_searched_transactions(
                filter_name=filter_name,
                pagination_query=pagination_query,
                transaction_task=transaction_task,
            )
            total_filtered_transactions.extend(filtered_transactions)

        return total_filtered_transactions

    def _find_searched_transactions(
        self,
        filter_name: TransactionFilterName,
        pagination_query: PaginationQueryFilter,
        transaction_task: OrderfulTransactionTask,
    ) -> list[dict[str, Any]]:
        transactions_per_page: TransactionsResponse = self._api_handler.get_transactions(
            pagination=pagination_query,
            query_filter=transaction_task.transaction_query,
        )
        transaction_filter: BaseTransactionFilter = get_transaction_filter_by_name(name=filter_name)
        searched_transaction = transaction_filter.filter(
            transaction_data=transactions_per_page.data,
            searched_text=transaction_task.searched_text,
        )

        return searched_transaction

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
