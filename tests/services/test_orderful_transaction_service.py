import pytest

from od_search.config import get_orderful_settings
from od_search.models.pagination import PaginationQueryFilter
from od_search.services.orderful_transaction_service import OrderfulTransactionService


@pytest.mark.parametrize(
    "expected, transactions_number",
    [
        (24, 2373),
        (1, 1),
    ],
)
def test_calculate_last_transaction_page_number(
    expected: int,
    transactions_number: int,
    orderful_transaction_service: OrderfulTransactionService,
) -> None:
    actual: int = orderful_transaction_service._calculate_last_transaction_page_number(
        number_checked_transactions=transactions_number
    )
    assert actual == expected


@pytest.mark.parametrize("invalid_transactions_number", [-1, 0])
def test_raise_validation_error_on_invalid_input_data(
    invalid_transactions_number: int,
    orderful_transaction_service: OrderfulTransactionService,
) -> None:
    with pytest.raises(ValueError):
        orderful_transaction_service._calculate_last_transaction_page_number(
            number_checked_transactions=invalid_transactions_number
        )


@pytest.mark.parametrize(
    "incoming_page_number, expected_offset, expected_total, ",
    [
        (1, 0, 100),
        (33, 3200, 3300),
        (41, 4000, 4100),
    ],
)
def test_create_pagination_query_minimal_data(
    incoming_page_number: int,
    expected_offset: int,
    expected_total: int,
    orderful_transaction_service: OrderfulTransactionService,
) -> None:
    expected = PaginationQueryFilter(
        offset=expected_offset,
        limit=get_orderful_settings().default_number_transaction_per_page,
        total=expected_total,
        links=None,
    )

    actual: PaginationQueryFilter = orderful_transaction_service._create_pagination_query(
        page_number=incoming_page_number
    )
    assert actual == expected
