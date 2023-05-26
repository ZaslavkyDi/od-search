from typing import Any

import pytest

from od_search.transaction_filters.json_implementation.to_filter import ToTransactionFilterJson


@pytest.fixture
def receiver_filter() -> ToTransactionFilterJson:
    return ToTransactionFilterJson()


def test_receiver_filter(
    transactions_response: dict[str, Any],
    receiver_filter: ToTransactionFilterJson,
) -> None:
    actual_result: list[dict[str, Any]] = receiver_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="124215133",
    )

    assert len(actual_result) == 4
    assert actual_result[0]["to"]["id"] == "124215133"
