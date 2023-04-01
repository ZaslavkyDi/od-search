import logging
from typing import Any


from od_search.models.requests import OrderfulTransactionTask
from od_search.models.responses import (
    OrderfulTransactionTaskResponse,
    OrderfulTransactionTaskMultipleFormatItemResponse,
)
from od_search.services.base_search_service import BaseSearchService


logger = logging.getLogger(__name__)


class JsonSearchService(BaseSearchService):
    async def search(
        self,
        search_task: OrderfulTransactionTask,
    ) -> OrderfulTransactionTaskResponse:
        total_filtered_transactions: list[dict[str, Any]] = []
        page_range = self._get_transactions_pages_range(search_task=search_task)

        async for transactions_per_page in self._get_transactions_per_page_range(
            page_range=page_range, transaction_query_filter=search_task.transaction_query
        ):
            filtered_transactions: list[dict[str, Any]] = self._filter_transactions(
                transactions_response=transactions_per_page,
                transaction_task=search_task,
            )
            total_filtered_transactions.extend(filtered_transactions)

        multi_format_transactions_data: list[OrderfulTransactionTaskMultipleFormatItemResponse] = [
            OrderfulTransactionTaskMultipleFormatItemResponse(
                json_format=i,
            )
            for i in total_filtered_transactions
        ]

        return OrderfulTransactionTaskResponse(
            metadata=search_task,
            total_items=len(multi_format_transactions_data),
            data=multi_format_transactions_data,
        )
