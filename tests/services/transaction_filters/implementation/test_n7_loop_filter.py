from typing import Any

import pytest

from od_search.transaction_filters.implementation.n7_loop_filter import (
    N7LoopTransactionFilter,
)
from tests.services.transaction_filters.utils import get_transaction_transaction_sets


@pytest.fixture
def n7_loop_filter() -> N7LoopTransactionFilter:
    return N7LoopTransactionFilter()


def test_n7_loop_filter(
    transactions_response: dict[str, Any],
    n7_loop_filter: N7LoopTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = n7_loop_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="unknown",
    )

    assert len(actual_result) == 3
    assert "unknown" == (
        get_transaction_transaction_sets(transaction_data=actual_result[0])["N7_loop"][0][
            "equipmentDetails"
        ][0]["equipmentNumber"]
    )
