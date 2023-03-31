from od_search.common.constants import JsonTransactionFilterNameFormat
from od_search.transaction_filters.base_filter import BaseTransactionFilter


class AT5LoopTransactionFilter(BaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(
            filter_name=JsonTransactionFilterNameFormat.AT5_LOOP, jpath_query="$..AT5_loop"
        )
