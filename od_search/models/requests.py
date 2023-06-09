from pydantic import BaseModel, Field

from od_search.config.constants import TransactionFilterNameOrderfulFormat
from od_search.models.api_handler.orderful.request import TransactionQueryFilter


class OrderfulTransactionTask(BaseModel):
    searched_filter: TransactionFilterNameOrderfulFormat | None = Field(None)
    searched_text: str | None = Field(None)
    number_checked_transactions: int = Field(
        100, description="A number of how many transactions need to be checked."
    )
    transaction_query: TransactionQueryFilter | None = Field(None)
