from pydantic import BaseModel, Field


class PaginationLink(BaseModel):
    next: str | None = Field(
        default=None,
        description="Link to the next page.",
    )
    prev: str | None = Field(
        default=None,
        description="Link to the prev page",
    )


class PaginationQueryFilter(BaseModel):
    offset: int = Field(default=0, description="Items skipping value.")
    limit: int = Field(default=100, description="Max items per page.")
    total: int = Field(default=0, description="Total items.")
    links: PaginationLink | None = Field(
        default=None, description="Links to the next and prev page if exists."
    )

    def to_request_query_format(self) -> dict[str, int]:
        return {
            "offset": self.offset,
            "limit": self.limit,
        }
