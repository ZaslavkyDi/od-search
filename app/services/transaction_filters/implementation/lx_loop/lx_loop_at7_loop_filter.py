from app.config.constants import TransactionFilterName
from app.services.transaction_filters.base_filter import BaseTransactionFilter


class LxLoopAt7LoopTransactionFilter(BaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(
            filter_name=TransactionFilterName.LX_LOOP_AT7_LOOP, jpath_query="$..LX_loop..AT7_loop"
        )
