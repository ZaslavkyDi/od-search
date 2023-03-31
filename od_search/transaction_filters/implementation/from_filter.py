from od_search.common.constants import JsonTransactionFilterNameFormat
from od_search.transaction_filters.base_filter import BaseTransactionFilter


class FromTransactionFilter(BaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(filter_name=JsonTransactionFilterNameFormat.FROM, jpath_query="from")
