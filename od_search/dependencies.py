from typing import Annotated

from fastapi import Depends, Path

from od_search.common.constants import TransactionFormat
from od_search.services.json_search_service import JsonSearchService
from od_search.services.x12_search_service import X12SearchService
from od_search.services.base_search_service import BaseSearchService


def get_search_service_by_transaction_format(
    json_service: Annotated[JsonSearchService, Depends(JsonSearchService)],
    x12_service: Annotated[X12SearchService, Depends(X12SearchService)],
    transaction_format: TransactionFormat = Path(...),
) -> BaseSearchService:
    format_to_service_map = {
        TransactionFormat.JSON.value: json_service,
        TransactionFormat.X12.value: x12_service,
    }
    return format_to_service_map[transaction_format]
