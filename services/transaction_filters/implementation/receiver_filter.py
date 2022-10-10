from services.transaction_filters.base_filter import BaseTransactionFilter


class ReceiverTransactionFilter(BaseTransactionFilter):

    def __init__(self) -> None:
        super().__init__(
            filter_name="to",
            jpath_query="to"
        )

