from typing import Any

import pytest

from app.services.transaction_filters.implementation.from_filter import FromTransactionFilter


@pytest.fixture
def sender_filter() -> FromTransactionFilter:
    return FromTransactionFilter()


def test_sender_filter(
    transactions_response: dict[str, Any],
    sender_filter: FromTransactionFilter,
) -> None:
    actual_result: list[dict[str, Any]] = sender_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="ZIPL",
    )

    assert len(actual_result) == 2
    assert actual_result[0]["from"]["id"] == "ZIPL"
