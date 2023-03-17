from typing import Any

import pytest

from od_search.services.transaction_filters.implementation.s5_loop.s5_loop_n1_loop_filter import (
    S5LoopN1LoopTransactionFilter,
)
from tests.services.transaction_filters.utils import get_transaction_transaction_sets


@pytest.fixture
def s5_loop_n1_loop_filter() -> S5LoopN1LoopTransactionFilter:
    return S5LoopN1LoopTransactionFilter()


def test_s5_loop_n1_loop_filter(
    transactions_response: dict[str, Any],
    s5_loop_n1_loop_filter: S5LoopN1LoopTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = s5_loop_n1_loop_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="BRWY-- St. Louis",
    )

    transaction_sets: dict[str, Any] = get_transaction_transaction_sets(
        transaction_data=actual_result[0]
    )

    assert len(actual_result) == 3
    assert "BRWY-- St. Louis" == (
        transaction_sets["S5_loop"][0]["N1_loop"][0]["contact"][0]["name"]
    )
    assert "BRWY-- St. Louis" == (
        transaction_sets["S5_loop"][0]["N1_loop"][0]["partyIdentification"][0]["name"]
    )
