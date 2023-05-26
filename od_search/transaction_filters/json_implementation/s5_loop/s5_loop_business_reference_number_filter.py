from od_search.common.constants import JsonTransactionFilterNameFormat
from od_search.transaction_filters.json_base_filter import JsonBaseTransactionFilter


class S5LoopBusinessInstructionAndReferenceNumbersTransactionFilterJson(JsonBaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(
            filter_name=JsonTransactionFilterNameFormat.S5_LOOP_BUSINESS_REFERENCE_NUMBER,
            jpath_query="$..S5_loop..businessInstructionsAndReferenceNumber",
        )