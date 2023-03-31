from typing import Any

import pytest

from od_search.transaction_filters.implementation import (
    BusinessInstructionAndReferenceNumbersTransactionFilter,
)
from tests.services.transaction_filters.utils import get_transaction_transaction_sets


@pytest.fixture
def business_reference_number_filter() -> BusinessInstructionAndReferenceNumbersTransactionFilter:
    return BusinessInstructionAndReferenceNumbersTransactionFilter()


def test_business_reference_number_filter(
    transactions_response: dict[str, Any],
    business_reference_number_filter: BusinessInstructionAndReferenceNumbersTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = business_reference_number_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="SW2558238",
    )

    assert len(actual_result) == 1
    assert "SW2558238" == (
        get_transaction_transaction_sets(transaction_data=actual_result[0])[
            "businessInstructionsAndReferenceNumber"
        ][0]["referenceIdentification"]
    )
