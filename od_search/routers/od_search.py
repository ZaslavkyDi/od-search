from typing import Annotated

from fastapi import APIRouter, Depends

from od_search.models.requests import OrderfulTransactionTask
from od_search.models.responses import OrderfulTransactionTaskEnums, OrderfulTransactionTaskResponse
from od_search.services.orderful_transaction_service import OrderfulTransactionService

router = APIRouter(prefix="/od-search", tags=["Orderful Dashboard Search"])


@router.post("")
async def search(
    task: OrderfulTransactionTask,
    transaction_service: Annotated[OrderfulTransactionService, Depends(OrderfulTransactionService)],
    include_x12: bool = False,
) -> OrderfulTransactionTaskResponse:
    return await transaction_service.search(search_task=task, include_x12=include_x12)


@router.get("/enums")
def show_searched_filter_enums() -> OrderfulTransactionTaskEnums:
    return OrderfulTransactionTaskEnums.build()
