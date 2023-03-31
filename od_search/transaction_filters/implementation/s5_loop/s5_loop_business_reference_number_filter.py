from od_search.common.constants import JsonTransactionFilterNameFormat
from od_search.transaction_filters.base_filter import BaseTransactionFilter


class S5LoopBusinessInstructionAndReferenceNumbersTransactionFilter(BaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(
            filter_name=JsonTransactionFilterNameFormat.S5_LOOP_BUSINESS_REFERENCE_NUMBER,
            jpath_query="$..S5_loop..businessInstructionsAndReferenceNumber",
        )
