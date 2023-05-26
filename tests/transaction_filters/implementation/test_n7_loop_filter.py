from typing import Any

import pytest

from od_search.transaction_filters.json_implementation.n7_loop_filter import (
    N7LoopTransactionFilterJson,
)
from transaction_filters.test_utils import get_transaction_transaction_sets


@pytest.fixture
def n7_loop_filter() -> N7LoopTransactionFilterJson:
    return N7LoopTransactionFilterJson()


def test_n7_loop_filter(
    transactions_response: dict[str, Any],
    n7_loop_filter: N7LoopTransactionFilterJson,
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
