from od_search.common.constants import TransactionFilterNameOrderfulFormat
from od_search.transaction_filters.base_filter import BaseTransactionFilter


class BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilter(
    BaseTransactionFilter
):
    def __init__(self) -> None:
        super().__init__(
            filter_name=TransactionFilterNameOrderfulFormat.CARRIER_SHIPMENT_STATUS_MESSAGE,
            jpath_query="$..beginningSegmentForTransportationCarrierShipmentStatusMessage",
        )
