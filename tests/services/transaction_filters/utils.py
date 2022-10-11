from typing import Any


def get_transaction_transaction_sets(transaction_data: dict[str, Any]) -> dict[str, Any]:
    return transaction_data["message"]["transactionSets"][0]
