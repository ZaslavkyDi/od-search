from typing import Any

import pytest

from od_search.transaction_filters.json_implementation.lx_loop.lx_loop_filter import (
    LxLoopTransactionFilterJson,
)
from transaction_filters.test_utils import get_transaction_transaction_sets


@pytest.fixture
def lx_loop_filter() -> LxLoopTransactionFilterJson:
    return LxLoopTransactionFilterJson()


def test_lx_loop_filter(
    transactions_response: dict[str, Any],
    lx_loop_filter: LxLoopTransactionFilterJson,
) -> None:
    actual_result: list[dict[str, Any]] = lx_loop_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text='"weight": "21000"',
    )

    assert len(actual_result) == 2
    assert "21000" == (
        get_transaction_transaction_sets(transaction_data=actual_result[0])["LX_loop"][0][
            "shipmentWeightPackagingAndQuantityData"
        ][0]["weight"]
    )
