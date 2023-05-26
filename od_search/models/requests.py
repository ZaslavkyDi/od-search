from typing import Literal

from pydantic import BaseModel, Field

from od_search.common.constants import JsonTransactionFilterNameFormat, TransactionFormat
from od_search.models.api_handler.orderful.request import TransactionQueryFilter


class BaseTransactionTask(BaseModel):
    transaction_format: TransactionFormat = Field(...)
    searched_filter: str = Field(...)
    searched_text: str | None = Field(None)
    transactions_offset: int = Field(
        0, description="A number of skipping transactions on Orderful dashboard."
    )
    transactions_for_check: int = Field(
        100, description="A number of how many transactions need to be checked."
    )
    transaction_query: TransactionQueryFilter | None = Field(None)


class JsonTransactionTask(BaseTransactionTask):
    transaction_format: Literal[TransactionFormat.JSON] = TransactionFormat.JSON
    searched_filter: JsonTransactionFilterNameFormat = Field(...)


class X12TransactionTask(BaseTransactionTask):
    transaction_format: Literal[TransactionFormat.X12] = TransactionFormat.X12
    searched_filter: str = Field(...)
