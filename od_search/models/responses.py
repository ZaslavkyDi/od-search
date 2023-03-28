from typing import Self, Any

from pydantic import BaseModel

from od_search.config.constants import (
    TransactionFilterNameOrderfulFormat,
    TransactionType,
    TransactionDirection,
)
from od_search.models.requests import OrderfulTransactionTask


class OrderfulTransactionTaskEnums(BaseModel):
    searched_filters: list[TransactionFilterNameOrderfulFormat]
    transaction_types: list[TransactionType]
    directions: list[TransactionDirection]

    @classmethod
    def build(cls) -> Self:
        return cls(
            searched_filters=[i for i in TransactionFilterNameOrderfulFormat],
            transaction_types=[i for i in TransactionType],
            directions=[i for i in TransactionDirection],
        )


class OrderfulTransactionTaskMultipleFormatItemResponse(BaseModel):
    json_format: dict[str, Any]
    x12_format: dict[str, Any] | None


class OrderfulTransactionTaskResponse(BaseModel):
    metadata: OrderfulTransactionTask
    total_items: int
    data: list[OrderfulTransactionTaskMultipleFormatItemResponse]
