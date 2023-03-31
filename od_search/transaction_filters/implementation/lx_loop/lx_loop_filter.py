from od_search.common.constants import TransactionFilterNameOrderfulFormat
from od_search.transaction_filters.base_filter import BaseTransactionFilter


class LxLoopTransactionFilter(BaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(
            filter_name=TransactionFilterNameOrderfulFormat.LX_LOOP_AT7_LOOP,
            jpath_query="$..LX_loop",
        )
