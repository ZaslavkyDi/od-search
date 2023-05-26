import re
from typing import Any


from od_search.transaction_filters.base_filter import BaseTransactionFilter


class X12TransactionFilter(BaseTransactionFilter):
    FILTER_REGEX_TEMPLATE = r"%s[*].*%s[*~]{1}"

    def __init__(self, searched_segment: str):
        if not searched_segment:
            raise ValueError("Param 'searched_segment' has to be populated!")

        self._searched_segment = searched_segment

    def filter(
        self,
        transaction_data: list[dict[str, Any]],
        searched_text: str,
    ) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        filter_regex: str = self.FILTER_REGEX_TEMPLATE % (self._searched_segment, searched_text)
        for transaction in transaction_data:
            match = re.search(pattern=filter_regex, string=transaction["message"])
            if match:
                results.append(transaction)

        return results
