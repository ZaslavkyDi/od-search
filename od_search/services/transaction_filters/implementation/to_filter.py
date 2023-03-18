from od_search.config.constants import TransactionFilterNameOrderfulFormat
from od_search.services.transaction_filters.base_filter import BaseTransactionFilter


class ToTransactionFilter(BaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(filter_name=TransactionFilterNameOrderfulFormat.TO, jpath_query="to")
