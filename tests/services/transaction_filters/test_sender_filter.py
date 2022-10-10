from typing import Any

import pytest

from services.transaction_filters.implementation.sender_filter import SenderTransactionFilter


@pytest.fixture
def sender_filter() -> SenderTransactionFilter:
    return SenderTransactionFilter()


def test_sender_filter(
        transactions_response: dict[str, Any],
        sender_filter: SenderTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = sender_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="ZIPL",
    )

    assert len(actual_result) == 2
    assert actual_result[0]["from"]["id"] == "ZIPL"


def test_sender_filter_none_items(
        transactions_response: dict[str, Any],
        sender_filter: SenderTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = sender_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="NONE_DATA",
    )
    assert len(actual_result) == 0
