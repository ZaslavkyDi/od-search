from typing import Self, Any

from pydantic import BaseModel

from od_search.common.constants import (
    JsonTransactionFilterNameFormat,
    TransactionType,
    TransactionDirection,
)
from od_search.models.requests import JsonTransactionTask


class OrderfulTransactionTaskEnums(BaseModel):
    searched_filters: list[JsonTransactionFilterNameFormat]
    transaction_types: list[TransactionType]
    directions: list[TransactionDirection]

    @classmethod
    def build(cls) -> Self:
        return cls(
            searched_filters=[i for i in JsonTransactionFilterNameFormat],
            transaction_types=[i for i in TransactionType],
            directions=[i for i in TransactionDirection],
        )


class OrderfulTransactionTaskMultipleFormatItemResponse(BaseModel):
    json_format: dict[str, Any] | None = None
    x12_format: dict[str, Any] | None = None


class OrderfulTransactionTaskResponse(BaseModel):
    metadata: JsonTransactionTask
    total_items: int
    data: list[OrderfulTransactionTaskMultipleFormatItemResponse]
