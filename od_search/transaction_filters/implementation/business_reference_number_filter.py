from od_search.common.constants import JsonTransactionFilterNameFormat
from od_search.transaction_filters.base_filter import BaseTransactionFilter


class BusinessInstructionAndReferenceNumbersTransactionFilter(BaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(
            filter_name=JsonTransactionFilterNameFormat.BUSINESS_REFERENCE_NUMBER,
            jpath_query="$..businessInstructionsAndReferenceNumber",
        )
