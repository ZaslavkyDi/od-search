from typing import Annotated

from fastapi import APIRouter, Depends

from od_search.dependencies import get_search_service_by_transaction_format
from od_search.models.requests import OrderfulTransactionTask
from od_search.models.responses import OrderfulTransactionTaskEnums, OrderfulTransactionTaskResponse
from od_search.services.base_search_service import BaseSearchService

router = APIRouter(prefix="/api/v1/od-search", tags=["Orderful Dashboard Search"])


@router.post("/{transaction_format}")
async def search(
    task: OrderfulTransactionTask,
    transaction_service: Annotated[
        BaseSearchService, Depends(get_search_service_by_transaction_format)
    ],
) -> OrderfulTransactionTaskResponse:
    return await transaction_service.search(search_task=task)


@router.get("/enums")
def show_searched_filter_enums() -> OrderfulTransactionTaskEnums:
    return OrderfulTransactionTaskEnums.build()
