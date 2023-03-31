from typing import Any

import pytest

from od_search.transaction_filters.implementation.lx_loop.lx_loop_at7_loop_filter import (
    LxLoopAt7LoopTransactionFilter,
)
from tests.services.transaction_filters.utils import get_transaction_transaction_sets


@pytest.fixture
def lx_loop_at7_loop_filter() -> LxLoopAt7LoopTransactionFilter:
    return LxLoopAt7LoopTransactionFilter()


def test_lx_loop_at7_loop_filter(
    transactions_response: dict[str, Any],
    lx_loop_at7_loop_filter: LxLoopAt7LoopTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = lx_loop_at7_loop_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="X6",
    )

    assert len(actual_result) == 10
    assert "X6" == (
        get_transaction_transaction_sets(transaction_data=actual_result[0])["LX_loop"][0][
            "AT7_loop"
        ][0]["shipmentStatusDetails"][0]["shipmentStatusIndicatorCode"]
    )
