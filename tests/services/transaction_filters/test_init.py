import pytest

from od_search.config.constants import TransactionFilterName
from od_search.services.transaction_filters import (
    get_all_transactions_filters,
    get_transaction_filter_by_name,
)


def test_get_all_transactions_filters() -> None:
    all_filters = get_all_transactions_filters()
    for name in TransactionFilterName:
        if name not in all_filters:
            raise AssertionError(f"Can not find transaction filter by name: {name.value!r}")

    assert True


@pytest.mark.parametrize(
    "filter_name",
    [
        TransactionFilterName.LX_LOOP_AT7_LOOP,
        TransactionFilterName.S5_LOOP,
        TransactionFilterName.BUSINESS_REFERENCE_NUMBER,
    ],
)
def test_get_transaction_filter_by_name(filter_name: TransactionFilterName) -> None:
    transaction_filter = get_transaction_filter_by_name(name=filter_name)
    assert transaction_filter


def test_get_transaction_filter_by_name_which_not_exist() -> None:
    with pytest.raises(KeyError):
        get_transaction_filter_by_name(name="Not Exists")
