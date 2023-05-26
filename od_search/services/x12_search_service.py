import logging
from typing import Any


from od_search.models.api_handler.orderful.response import (
    TransactionsResponse,
    TransactionX12AttachmentResponse,
)
from od_search.models.requests import JsonTransactionTask
from od_search.models.responses import (
    OrderfulTransactionTaskResponse,
    OrderfulTransactionTaskMultipleFormatItemResponse,
)
from od_search.services.base_search_service import BaseSearchService
from od_search.transaction_filters.x12_filter import X12TransactionFilter

logger = logging.getLogger(__name__)


class X12SearchService(BaseSearchService):
    async def search(
        self,
        search_task: JsonTransactionTask,
    ) -> OrderfulTransactionTaskResponse:
        total_filtered_transactions: list[dict[str, Any]] = []
        page_range = self._get_transactions_pages_range(search_task=search_task)

        async for transactions_page_response in self._get_transactions_per_page_range(
            page_range=page_range, transaction_query_filter=search_task.transaction_query
        ):
            transactions_with_attachments = self._remove_transactions_without_attachments(
                transactions_response=transactions_page_response
            )
            x12_transactions = await self._get_transactions_x12_format(
                transactions_response=transactions_with_attachments,
            )
            filtered_transactions: list[dict[str, Any]] = self._filter_transactions(
                transactions=x12_transactions,
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
        transactions: list[TransactionX12AttachmentResponse],
        transaction_task: JsonTransactionTask,
    ) -> list[dict[str, Any]]:
        transaction_filter = X12TransactionFilter(searched_segment=transaction_task.searched_filter)

        transaction_data: list[dict[str, Any]] = [i.dict() for i in transactions]
        searched_transaction = transaction_filter.filter(
            transaction_data=transaction_data,
            searched_text=transaction_task.searched_text,
        )

        return searched_transaction

    @staticmethod
    def _remove_transactions_without_attachments(
        transactions_response: TransactionsResponse,
    ) -> TransactionsResponse:
        transactions_with_attachments = [
            transaction
            for transaction in transactions_response.data
            if "attachments" in transaction["links"]
        ]

        transactions_response.data = transactions_with_attachments
        return transactions_response

    async def _get_transactions_x12_format(
        self, transactions_response: TransactionsResponse
    ) -> list[TransactionX12AttachmentResponse]:
        x12_formats: list[TransactionX12AttachmentResponse] = []
        for transaction in transactions_response.data:
            transaction_id: int = transaction["id"]
            try:
                response = await self._api_handler.get_x12_transaction(
                    transaction_id=transaction_id
                )
                x12_formats.append(response)
            except ValueError:
                logger.warning(f"Can not find x12 format for transaction id: {transaction_id}")

        return x12_formats
