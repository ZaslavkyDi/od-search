from od_search.config.constants import TransactionFilterNameOrderfulFormat
from od_search.services.transaction_filters.base_filter import BaseTransactionFilter


class S5LoopN1LoopTransactionFilter(BaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(
            filter_name=TransactionFilterNameOrderfulFormat.S5_LOOP_N1_LOOP,
            jpath_query="$..S5_loop..N1_loop",
        )
