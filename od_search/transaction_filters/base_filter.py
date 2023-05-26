import abc
from typing import Any, Protocol


class BaseTransactionFilter(Protocol, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def filter(
        self, transaction_data: list[dict[str, Any]], searched_text: str
    ) -> list[dict[str, Any]]:
        """
        Filtering given transaction data by specific searched text in specific transaction segment.

        example:
            Search "AIIH" sender in given transactions
            {
                "id": 104922259,
                "from": {
                    "idType": "isaId",
                    "id": "AIIH"
                },
                "to": {
                    "idType": "isaId",
                    "id": "OLGA"
                },
                "stream": "live",
                ...
            }

        result:
            Return list with transactions that contains "AIIH" in segment path "from"
        """
        pass
