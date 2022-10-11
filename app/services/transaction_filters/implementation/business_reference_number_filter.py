from app.config.constants import TransactionFilterName
from app.services.transaction_filters.base_filter import BaseTransactionFilter


class BusinessInstructionAndReferenceNumbersTransactionFilter(BaseTransactionFilter):

    def __init__(self) -> None:
        super().__init__(
            filter_name=TransactionFilterName.BUSINESS_REFERENCE_NUMBER,
            jpath_query="$..businessInstructionsAndReferenceNumber"
        )
