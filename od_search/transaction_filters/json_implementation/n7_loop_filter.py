from od_search.common.constants import JsonTransactionFilterNameFormat
from od_search.transaction_filters.json_base_filter import JsonBaseTransactionFilter


class N7LoopTransactionFilterJson(JsonBaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(
            filter_name=JsonTransactionFilterNameFormat.N7_LOOP, jpath_query="$..N7_loop"
        )
