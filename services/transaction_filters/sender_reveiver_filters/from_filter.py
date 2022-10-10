from abc import ABC
from typing import Any

from services.transaction_filters.base_filter import BaseTransactionFilter


class BaseSenderReceiverTransactionFilter(BaseTransactionFilter, ABC):

    def __init__(self, filter_name: str) -> None:
        super().__init__(filter_name=filter_name)

    def filter(self, transaction_data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        pass
