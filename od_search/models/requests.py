from pydantic import BaseModel, Field

from od_search.common.constants import JsonTransactionFilterNameFormat
from od_search.models.api_handler.orderful.request import TransactionQueryFilter


class OrderfulTransactionTask(BaseModel):
    searched_filter: JsonTransactionFilterNameFormat | None = Field(None)
    searched_text: str | None = Field(None)
    transactions_offset: int = Field(
        0, description="A number of skipping transactions on Orderful dashboard."
    )
    transactions_for_check: int = Field(
        100, description="A number of how many transactions need to be checked."
    )
    transaction_query: TransactionQueryFilter | None = Field(None)
