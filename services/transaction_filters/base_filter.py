from abc import ABC, abstractmethod
from typing import Any


class BaseTransactionFilter(ABC):

    def __init__(self, filter_name: str) -> None:
        if not filter_name:
            raise ValueError("Param 'filter_name' has to be populated!")
        self._filter_name = filter_name

    @property
    def filter_name(self) -> str:
        return self._filter_name

    @abstractmethod
    def filter(self, transaction_data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        pass
