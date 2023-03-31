from od_search.common.constants import JsonTransactionFilterNameFormat
from od_search.transaction_filters.base_filter import BaseTransactionFilter


class BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilter(
    BaseTransactionFilter
):
    def __init__(self) -> None:
        super().__init__(
            filter_name=JsonTransactionFilterNameFormat.CARRIER_SHIPMENT_STATUS_MESSAGE,
            jpath_query="$..beginningSegmentForTransportationCarrierShipmentStatusMessage",
        )
