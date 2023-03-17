from od_search.config.constants import TransactionFilterName
from od_search.services.transaction_filters.base_filter import BaseTransactionFilter


class BusinessInstructionAndReferenceNumbersTransactionFilter(BaseTransactionFilter):
    def __init__(self) -> None:
        super().__init__(
            filter_name=TransactionFilterName.BUSINESS_REFERENCE_NUMBER,
            jpath_query="$..businessInstructionsAndReferenceNumber",
        )
