from functools import lru_cache

from od_search.common.constants import TransactionFilterNameOrderfulFormat
from od_search.transaction_filters.base_filter import BaseTransactionFilter
from od_search.transaction_filters.implementation.at5_loop_filter import (
    AT5LoopTransactionFilter,
)
from od_search.transaction_filters.implementation.business_reference_number_filter import (
    BusinessInstructionAndReferenceNumbersTransactionFilter,
)
from od_search.transaction_filters.implementation.carrier_shipment_status_message_filter import (
    BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilter,
)
from od_search.transaction_filters.implementation.from_filter import FromTransactionFilter
from od_search.transaction_filters.implementation.lx_loop.lx_loop_at7_loop_filter import (
    LxLoopAt7LoopTransactionFilter,
)
from od_search.transaction_filters.implementation.lx_loop.lx_loop_filter import (
    LxLoopTransactionFilter,
)
from od_search.transaction_filters.implementation.n1_loop_filter import (
    N1LoopTransactionFilter,
)
from od_search.transaction_filters.implementation.n7_loop_filter import (
    N7LoopTransactionFilter,
)
from od_search.transaction_filters.implementation.s5_loop.s5_loop_business_reference_number_filter import (
    S5LoopBusinessInstructionAndReferenceNumbersTransactionFilter,
)
from od_search.transaction_filters.implementation.s5_loop.s5_loop_filter import (
    S5LoopTransactionFilter,
)
from od_search.transaction_filters.implementation.s5_loop.s5_loop_n1_loop_filter import (
    S5LoopN1LoopTransactionFilter,
)
from od_search.transaction_filters.implementation.to_filter import ToTransactionFilter


@lru_cache
def get_all_transactions_filters() -> (
    dict[TransactionFilterNameOrderfulFormat, BaseTransactionFilter]
):
    return {
        TransactionFilterNameOrderfulFormat.TO: ToTransactionFilter(),
        TransactionFilterNameOrderfulFormat.FROM: FromTransactionFilter(),
        TransactionFilterNameOrderfulFormat.N1_LOOP: N1LoopTransactionFilter(),
        TransactionFilterNameOrderfulFormat.N7_LOOP: N7LoopTransactionFilter(),
        TransactionFilterNameOrderfulFormat.BUSINESS_REFERENCE_NUMBER: BusinessInstructionAndReferenceNumbersTransactionFilter(),
        TransactionFilterNameOrderfulFormat.CARRIER_SHIPMENT_STATUS_MESSAGE: BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilter(),
        TransactionFilterNameOrderfulFormat.LX_LOOP: LxLoopTransactionFilter(),
        TransactionFilterNameOrderfulFormat.LX_LOOP_AT7_LOOP: LxLoopAt7LoopTransactionFilter(),
        TransactionFilterNameOrderfulFormat.S5_LOOP: S5LoopTransactionFilter(),
        TransactionFilterNameOrderfulFormat.S5_LOOP_N1_LOOP: S5LoopN1LoopTransactionFilter(),
        TransactionFilterNameOrderfulFormat.S5_LOOP_BUSINESS_REFERENCE_NUMBER: S5LoopBusinessInstructionAndReferenceNumbersTransactionFilter(),
        TransactionFilterNameOrderfulFormat.AT5_LOOP: AT5LoopTransactionFilter(),
    }


def get_transaction_filter_by_name(
    name: TransactionFilterNameOrderfulFormat,
) -> BaseTransactionFilter:
    return get_all_transactions_filters()[name]
