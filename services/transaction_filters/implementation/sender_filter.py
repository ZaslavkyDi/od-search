from abc import ABC
from typing import Any

from services.transaction_filters.base_filter import BaseTransactionFilter


class SenderTransactionFilter(BaseTransactionFilter):

    def __init__(self) -> None:
        super().__init__(
            filter_name="from",
            jpath_query="from"
        )
