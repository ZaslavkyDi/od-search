from od_search.config.constants import TransactionFilterName
from od_search.services.transaction_filters.base_filter import BaseTransactionFilter


class N7LoopTransactionFilter(BaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(filter_name=TransactionFilterName.N7_LOOP, jpath_query="$..N7_loop")
