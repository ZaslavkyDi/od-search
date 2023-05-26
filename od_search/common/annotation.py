from typing import Annotated

from pydantic import Field

from od_search.models.requests import X12TransactionTask, JsonTransactionTask

SubTransactionTaskAnnotation = Annotated[
    JsonTransactionTask | X12TransactionTask,
    Field(discriminator="transaction_format"),
]
