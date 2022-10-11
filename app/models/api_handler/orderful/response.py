from typing import Any

from pydantic import BaseModel, Field

from app.models.pagination import PaginationQueryFilter


class TransactionsResponseQuery(BaseModel):
    limit: int = Field(default=100)
    offset: int = Field(default=0)
    ownerId: int = Field(default=0)


class TransactionsResponse(BaseModel):
    query: TransactionsResponseQuery = Field(...)
    pagination: PaginationQueryFilter = Field(...)
    data: list[dict[str, Any]] = Field(...)
