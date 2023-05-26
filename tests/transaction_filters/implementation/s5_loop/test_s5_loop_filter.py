from typing import Any

import pytest

from od_search.transaction_filters.json_implementation.s5_loop.s5_loop_filter import (
    S5LoopTransactionFilterJson,
)
from transaction_filters.test_utils import get_transaction_transaction_sets


@pytest.fixture
def s5_loop_filter() -> S5LoopTransactionFilterJson:
    return S5LoopTransactionFilterJson()


def test_s5_loop_filter(
    transactions_response: dict[str, Any],
    s5_loop_filter: S5LoopTransactionFilterJson,
) -> None:
    actual_result: list[dict[str, Any]] = s5_loop_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text='"stopSequenceNumber": "1"',
    )

    assert len(actual_result) == 3
    assert "1" == (
        get_transaction_transaction_sets(transaction_data=actual_result[0])["S5_loop"][0][
            "stopOffDetails"
        ][0]["stopSequenceNumber"]
    )
