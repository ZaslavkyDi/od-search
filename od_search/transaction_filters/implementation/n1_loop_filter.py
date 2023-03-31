from od_search.common.constants import JsonTransactionFilterNameFormat
from od_search.transaction_filters.base_filter import BaseTransactionFilter


class N1LoopTransactionFilter(BaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(
            filter_name=JsonTransactionFilterNameFormat.N1_LOOP, jpath_query="$..N1_loop"
        )
