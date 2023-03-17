from typing import Any

import pytest

from app.services.transaction_filters.implementation.lx_loop.lx_loop_filter import (
    LxLoopTransactionFilter,
)
from app.services.transaction_filters.implementation.n1_loop_filter import N1LoopTransactionFilter
from tests.services.transaction_filters.utils import get_transaction_transaction_sets


@pytest.fixture
def n1_loop_filter() -> N1LoopTransactionFilter:
    return N1LoopTransactionFilter()


def test_n1_loop_filter(
    transactions_response: dict[str, Any],
    n1_loop_filter: LxLoopTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = n1_loop_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="62b908c6-0699-4626-ae00-8e44764f85cb",
    )

    assert len(actual_result) == 1
    assert "62b908c6-0699-4626-ae00-8e44764f85cb" == (
        get_transaction_transaction_sets(transaction_data=actual_result[0])["N1_loop"][0][
            "partyIdentification"
        ][0]["identificationCode"]
    )
