from typing import Any

import pytest

from app.services.transaction_filters.implementation.carrier_shipment_status_message_filter import (
    BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilter,
)
from tests.services.transaction_filters.utils import get_transaction_transaction_sets


@pytest.fixture
def carrier_shipment_status_message_filter() -> (
    BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilter
):
    return BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilter()


def test_business_reference_number_filter(
    transactions_response: dict[str, Any],
    carrier_shipment_status_message_filter: BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = carrier_shipment_status_message_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="B6RBUY",
    )

    assert len(actual_result) == 3
    assert "B6RBUY" == (
        get_transaction_transaction_sets(transaction_data=actual_result[0])[
            "beginningSegmentForTransportationCarrierShipmentStatusMessage"
        ][0]["referenceIdentification"]
    )
