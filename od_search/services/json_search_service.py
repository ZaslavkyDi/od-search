import logging
from typing import Any


from od_search.models.requests import JsonTransactionTask
from od_search.models.responses import (
    OrderfulTransactionTaskResponse,
    OrderfulTransactionTaskMultipleFormatItemResponse,
)
from od_search.services.base_search_service import BaseSearchService
from od_search.transaction_filters import (
    JsonBaseTransactionFilter,
    get_json_transaction_filter_by_name,
)

logger = logging.getLogger(__name__)


class JsonSearchService(BaseSearchService):
    async def search(
        self,
        search_task: JsonTransactionTask,
    ) -> OrderfulTransactionTaskResponse:
        total_filtered_transactions: list[dict[str, Any]] = []
        page_range = self._get_transactions_pages_range(search_task=search_task)

        async for transactions_page_response in self._get_transactions_per_page_range(
            page_range=page_range, transaction_query_filter=search_task.transaction_query
        ):
            filtered_transactions = self._filter_transactions(
                transactions=transactions_page_response,
                transaction_task=search_task,
            )
            total_filtered_transactions.extend(filtered_transactions)

        multi_format_transactions_data: list[OrderfulTransactionTaskMultipleFormatItemResponse] = []
        for transactions_page_response in total_filtered_transactions:
            multi_format_transactions_data.append(
                OrderfulTransactionTaskMultipleFormatItemResponse(
                    json_format=transactions_page_response,
                )
            )

        return OrderfulTransactionTaskResponse(
            metadata=search_task,
            total_items=len(multi_format_transactions_data),
            data=multi_format_transactions_data,
        )

    def _filter_transactions(
        self,
        transactions: Any,
        transaction_task: JsonTransactionTask,
    ) -> list[dict[str, Any]]:
        transaction_filter: JsonBaseTransactionFilter = get_json_transaction_filter_by_name(
            name=transaction_task.searched_filter
        )
        searched_transaction = transaction_filter.filter(
            transaction_data=transactions.data,
            searched_text=transaction_task.searched_text,
        )

        return searched_transaction
