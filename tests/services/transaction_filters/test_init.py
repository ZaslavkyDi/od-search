import pytest

from od_search.common.constants import TransactionFilterNameOrderfulFormat
from od_search.services.transaction_filters import (
    get_all_transactions_filters,
    get_transaction_filter_by_name,
)


def test_get_all_transactions_filters() -> None:
    all_filters = get_all_transactions_filters()
    for name in TransactionFilterNameOrderfulFormat:
        if name not in all_filters:
            raise AssertionError(f"Can not find transaction filter by name: {name.value!r}")

    assert True


@pytest.mark.parametrize(
    "filter_name",
    [
        TransactionFilterNameOrderfulFormat.LX_LOOP_AT7_LOOP,
        TransactionFilterNameOrderfulFormat.S5_LOOP,
        TransactionFilterNameOrderfulFormat.BUSINESS_REFERENCE_NUMBER,
    ],
)
def test_get_transaction_filter_by_name(filter_name: TransactionFilterNameOrderfulFormat) -> None:
    transaction_filter = get_transaction_filter_by_name(name=filter_name)
    assert transaction_filter


def test_get_transaction_filter_by_name_which_not_exist() -> None:
    with pytest.raises(KeyError):
        get_transaction_filter_by_name(name="Not Exists")
