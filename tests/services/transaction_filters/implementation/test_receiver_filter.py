from typing import Any

import pytest

from od_search.services.transaction_filters.implementation.to_filter import ToTransactionFilter


@pytest.fixture
def receiver_filter() -> ToTransactionFilter:
    return ToTransactionFilter()


def test_receiver_filter(
    transactions_response: dict[str, Any],
    receiver_filter: ToTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = receiver_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="124215133",
    )

    assert len(actual_result) == 4
    assert actual_result[0]["to"]["id"] == "124215133"
