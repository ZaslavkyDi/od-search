from app.config.constants import TransactionFilterName
from app.services.transaction_filters.base_filter import BaseTransactionFilter


class N1LoopTransactionFilter(BaseTransactionFilter):

    def __init__(self) -> None:
        super().__init__(
            filter_name=TransactionFilterName.N1_LOOP,
            jpath_query="$..N1_loop"
        )
