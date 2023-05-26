from typing import Any

import pytest

from od_search.transaction_filters.json_implementation import (
    S5LoopBusinessInstructionAndReferenceNumbersTransactionFilter,
)
from transaction_filters.test_utils import get_transaction_transaction_sets


@pytest.fixture
def s5_loop_business_reference_number_filter() -> (
    S5LoopBusinessInstructionAndReferenceNumbersTransactionFilter
):
    return S5LoopBusinessInstructionAndReferenceNumbersTransactionFilter()


def test_s5_loop_n1_loop_filter(
    transactions_response: dict[str, Any],
    s5_loop_business_reference_number_filter: S5LoopBusinessInstructionAndReferenceNumbersTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = s5_loop_business_reference_number_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text='"referenceIdentificationQualifier": "QN"',
    )

    transaction_sets: dict[str, Any] = get_transaction_transaction_sets(
        transaction_data=actual_result[0]
    )

    assert len(actual_result) == 3
    assert "QN" == (
        transaction_sets["S5_loop"][0]["businessInstructionsAndReferenceNumber"][0][
            "referenceIdentificationQualifier"
        ]
    )
