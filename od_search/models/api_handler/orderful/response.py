from typing import Any, Literal

from pydantic import BaseModel, Field

from od_search.models.pagination import PaginationQueryFilter


class TransactionsResponseQuery(BaseModel):
    limit: int = Field(default=100)
    offset: int = Field(default=0)
    ownerId: int = Field(default=0)


class TransactionsResponse(BaseModel):
    query: TransactionsResponseQuery = Field(...)
    pagination: PaginationQueryFilter = Field(...)
    data: list[dict[str, Any]] = Field(...)


class TransactionX12AttachmentResponse(BaseModel):
    id: int = Field(...)
    format: Literal["x12"] = Field("x12")
    message: str = Field(...)
    name: str = Field("Generated X12")
