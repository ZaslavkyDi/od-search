from functools import lru_cache

from app.config.constants import TransactionFilterName
from app.services.transaction_filters.base_filter import BaseTransactionFilter
from app.services.transaction_filters.implementation.business_reference_number_filter import \
    BusinessInstructionAndReferenceNumbersTransactionFilter
from app.services.transaction_filters.implementation.carrier_shipment_status_message_filter import \
    BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilter
from app.services.transaction_filters.implementation.from_filter import FromTransactionFilter
from app.services.transaction_filters.implementation.lx_loop.lx_loop_at7_loop_filter import \
    LxLoopAt7LoopTransactionFilter
from app.services.transaction_filters.implementation.lx_loop.lx_loop_filter import LxLoopTransactionFilter
from app.services.transaction_filters.implementation.n1_loop_filter import N1LoopTransactionFilter
from app.services.transaction_filters.implementation.n7_loop_filter import N7LoopTransactionFilter
from app.services.transaction_filters.implementation.s5_loop.s5_loop_business_reference_number_filter import \
    S5LoopBusinessInstructionAndReferenceNumbersTransactionFilter
from app.services.transaction_filters.implementation.s5_loop.s5_loop_filter import S5LoopTransactionFilter
from app.services.transaction_filters.implementation.s5_loop.s5_loop_n1_loop_filter import S5LoopN1LoopTransactionFilter
from app.services.transaction_filters.implementation.to_filter import ToTransactionFilter


@lru_cache
def get_all_transactions_filters() -> dict[TransactionFilterName, BaseTransactionFilter]:
    return {
        TransactionFilterName.TO: ToTransactionFilter(),
        TransactionFilterName.FROM: FromTransactionFilter(),
        TransactionFilterName.N1_LOOP: N1LoopTransactionFilter(),
        TransactionFilterName.N7_LOOP: N7LoopTransactionFilter(),
        TransactionFilterName.BUSINESS_REFERENCE_NUMBER: BusinessInstructionAndReferenceNumbersTransactionFilter(),
        TransactionFilterName.CARRIER_SHIPMENT_STATUS_MESSAGE: BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilter(),
        TransactionFilterName.LX_LOOP: LxLoopTransactionFilter(),
        TransactionFilterName.LX_LOOP_AT7_LOOP: LxLoopAt7LoopTransactionFilter(),
        TransactionFilterName.S5_LOOP: S5LoopTransactionFilter(),
        TransactionFilterName.S5_LOOP_N1_LOOP: S5LoopN1LoopTransactionFilter(),
        TransactionFilterName.S5_LOOP_BUSINESS_REFERENCE_NUMBER: S5LoopBusinessInstructionAndReferenceNumbersTransactionFilter(),
    }


def get_transaction_filter_by_name(name: TransactionFilterName) -> BaseTransactionFilter:
    return get_all_transactions_filters()[name]
