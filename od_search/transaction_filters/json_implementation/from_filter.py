from od_search.common.constants import JsonTransactionFilterNameFormat
from od_search.transaction_filters.json_base_filter import JsonBaseTransactionFilter


class FromTransactionFilterJson(JsonBaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(filter_name=JsonTransactionFilterNameFormat.FROM, jpath_query="from")
