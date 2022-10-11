from app.config.constants import TransactionFilterName
from app.services.transaction_filters.base_filter import BaseTransactionFilter


class BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilter(BaseTransactionFilter):

    def __init__(self) -> None:
        super().__init__(
            filter_name=TransactionFilterName.CARRIER_SHIPMENT_STATUS_MESSAGE,
            jpath_query="$..beginningSegmentForTransportationCarrierShipmentStatusMessage"
        )
