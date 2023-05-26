from typing import Annotated, TypeVar

from fastapi import Depends

from od_search.common.constants import TransactionFormat
from od_search.models.requests import BaseTransactionTask, JsonTransactionTask, X12TransactionTask
from od_search.services.json_search_service import JsonSearchService
from od_search.services.x12_search_service import X12SearchService
from od_search.services.base_search_service import BaseSearchService

SubTransactionTask = TypeVar("SubTransactionTask", bound=BaseTransactionTask)


def get_search_service_by_transaction_format(
    json_service: Annotated[JsonSearchService, Depends(JsonSearchService)],
    x12_service: Annotated[X12SearchService, Depends(X12SearchService)],
    task: JsonTransactionTask | X12TransactionTask,
) -> BaseSearchService:
    format_to_service_map = {
        TransactionFormat.JSON.value: json_service,
        TransactionFormat.X12.value: x12_service,
    }
    return format_to_service_map[task.transaction_format]
