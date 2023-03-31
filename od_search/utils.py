from functools import lru_cache

from od_search.common.constants import TransactionTypeIdOrderfulFormat, TransactionType


@lru_cache
def convert_transaction_type_to_orderful_query_format(
    transaction_type: TransactionType,
) -> TransactionTypeIdOrderfulFormat:
    ttype_to_orderful_map = {
        TransactionType.TYPE_204_ID: TransactionTypeIdOrderfulFormat.TYPE_204_ID,
        TransactionType.TYPE_214_ID: TransactionTypeIdOrderfulFormat.TYPE_214_ID,
        TransactionType.TYPE_210_ID: TransactionTypeIdOrderfulFormat.TYPE_210_ID,
        TransactionType.TYPE_990_ID: TransactionTypeIdOrderfulFormat.TYPE_990_ID,
    }
    return ttype_to_orderful_map[transaction_type]
