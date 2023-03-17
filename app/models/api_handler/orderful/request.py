from pydantic import BaseModel, Field

from app.config.constants import TransactionTypeId, TransactionDirection


class TransactionQueryFilter(BaseModel):
    business_number: str | None = Field(
        default=None,
        description="Orderful transaction business number.",
    )
    transaction_type: TransactionTypeId | None = Field(
        default=None,
        description="Orderful transaction type id 18/19/20/34.",
    )
    direction: TransactionDirection | None = Field(
        default=None,
        description="Orderful transaction direction in/out.",
    )

    def to_request_query_format(self) -> dict[str, str | int | None]:
        return {
            "businessNumber": self.business_number,
            "transactionTypeId": self.transaction_type.value if self.transaction_type else None,
            "direction": self.direction.value if self.direction else None,
        }

    def to_request_not_none_query_format(self) -> dict[str, str | int]:
        query_data = self.to_request_query_format()
        return {k: v for k, v in query_data.items() if v is not None}
