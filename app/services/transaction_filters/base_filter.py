import json
from abc import ABC
from typing import Any

import jsonpath_ng as jpath

from app.config.constants import TransactionFilterName


class BaseTransactionFilter(ABC):

    def __init__(self, filter_name: TransactionFilterName, jpath_query: str) -> None:
        if not filter_name:
            raise ValueError("Param 'filter_name' has to be populated!")

        if not jpath_query:
            raise ValueError("Param 'jpath_query' has to be populated!")

        self._filter_name = filter_name
        self._jsonpath_expr = jpath.parse(jpath_query)

    @property
    def filter_name(self) -> TransactionFilterName:
        return self._filter_name

    def filter(self, transaction_data: list[dict[str, Any]], searched_text: str) -> list[dict[str, Any]]:
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
        results: list[dict[str, Any]] = []
        for transaction in transaction_data:
            matches = self._jsonpath_expr.find(transaction)
            if len(matches) == 0:
                continue

            has_match = False
            for match in matches:
                json_string: str = json.dumps(match.value)
                if searched_text in json_string:
                    has_match = True
                    break

            if has_match:
                results.append(transaction)

        return results
