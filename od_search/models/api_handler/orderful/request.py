from pydantic import BaseModel, Field

from od_search.config.constants import (
    TransactionTypeIdOrderfulFormat,
    TransactionDirection,
    TransactionType,
)
from od_search.utils import convert_transaction_type_to_orderful_query_format


class TransactionQueryFilter(BaseModel):
    business_number: str | None = Field(
        default=None,
        description="Orderful transaction business number.",
    )
    transaction_type: TransactionType | None = Field(
        default=None,
        description="Orderful transaction type id 18/19/20/34.",
    )
    direction: TransactionDirection | None = Field(
        default=None,
        description="Orderful transaction direction in/out.",
    )

    def to_request_query_format(self) -> dict[str, str | int | None]:
        orderful_transaction_type: TransactionTypeIdOrderfulFormat | None = None
        if self.transaction_type:
            orderful_transaction_type = convert_transaction_type_to_orderful_query_format(
                self.transaction_type
            )

        return {
            "businessNumber": self.business_number,
            "transactionTypeId": orderful_transaction_type.value,
            "direction": self.direction.value if self.direction else None,
        }

    def to_request_not_none_query_format(self) -> dict[str, str | int]:
        query_data = self.to_request_query_format()
        return {k: v for k, v in query_data.items() if v is not None}
