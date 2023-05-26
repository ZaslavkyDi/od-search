from typing import Any

import pytest

from od_search.transaction_filters.x12_filter import X12TransactionFilter


@pytest.mark.parametrize(
    "searched_segment, searched_text, expected_result_count",
    [
        ("AK1", "1271789", 1),
        ("AK5", "A", 8),
    ],
)
def test_filter(
    searched_segment: str,
    searched_text: str,
    expected_result_count: int,
    x12_transactions_response: list[dict[str, Any]],
) -> None:
    x12_filter = X12TransactionFilter(searched_segment=searched_segment)
    actual: list[dict[str, Any]] = x12_filter.filter(
        transaction_data=x12_transactions_response,
        searched_text=searched_text,
    )

    assert len(actual) == expected_result_count
