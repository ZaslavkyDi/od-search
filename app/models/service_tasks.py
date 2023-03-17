from pydantic import BaseModel, Field

from app.models.api_handler.orderful.request import TransactionQueryFilter


class OrderfulTransactionTask(BaseModel):
    searched_text: str = Field(...)
    number_checked_transactions: int = Field(
        100,
        description="A number of how many transactions need to be checked."
    )
    transaction_query: TransactionQueryFilter | None = Field(None)
