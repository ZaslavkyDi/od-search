from typing import Any

import pytest

from services.transaction_filters.implementation.receiver_filter import ReceiverTransactionFilter


@pytest.fixture
def receiver_filter() -> ReceiverTransactionFilter:
    return ReceiverTransactionFilter()


def test_receiver_filter(
        transactions_response: dict[str, Any],
        receiver_filter: ReceiverTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = receiver_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="124215133",
    )

    assert len(actual_result) == 4
    assert actual_result[0]["to"]["id"] == "124215133"


def test_receiver_filter_none_items(
        transactions_response: dict[str, Any],
        receiver_filter: ReceiverTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = receiver_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="NONE_DATA",
    )
    assert len(actual_result) == 0
