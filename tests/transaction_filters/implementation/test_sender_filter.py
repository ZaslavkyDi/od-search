from typing import Any

import pytest

from od_search.transaction_filters.json_implementation.from_filter import FromTransactionFilterJson


@pytest.fixture
def sender_filter() -> FromTransactionFilterJson:
    return FromTransactionFilterJson()


def test_sender_filter(
    transactions_response: dict[str, Any],
    sender_filter: FromTransactionFilterJson,
) -> None:
    actual_result: list[dict[str, Any]] = sender_filter.filter(
        transaction_data=transactions_response["data"],
        searched_text="ZIPL",
    )

    assert len(actual_result) == 2
    assert actual_result[0]["from"]["id"] == "ZIPL"
