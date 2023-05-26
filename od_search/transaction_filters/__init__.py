from functools import lru_cache

from od_search.common.constants import JsonTransactionFilterNameFormat
from od_search.transaction_filters.json_base_filter import JsonBaseTransactionFilter
from od_search.transaction_filters.json_implementation.at5_loop_filter import (
    AT5LoopTransactionFilterJson,
)
from od_search.transaction_filters.json_implementation.business_reference_number_filter import (
    BusinessInstructionAndReferenceNumbersTransactionFilterJson,
)
from od_search.transaction_filters.json_implementation.carrier_shipment_status_message_filter import (
    BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilterJson,
)
from od_search.transaction_filters.json_implementation.from_filter import FromTransactionFilterJson
from od_search.transaction_filters.json_implementation.lx_loop.lx_loop_at7_loop_filter import (
    LxLoopAt7LoopTransactionFilterJson,
)
from od_search.transaction_filters.json_implementation.lx_loop.lx_loop_filter import (
    LxLoopTransactionFilterJson,
)
from od_search.transaction_filters.json_implementation.n1_loop_filter import (
    N1LoopTransactionFilterJson,
)
from od_search.transaction_filters.json_implementation.n7_loop_filter import (
    N7LoopTransactionFilterJson,
)
from od_search.transaction_filters.json_implementation.s5_loop.s5_loop_business_reference_number_filter import (
    S5LoopBusinessInstructionAndReferenceNumbersTransactionFilterJson,
)
from od_search.transaction_filters.json_implementation.s5_loop.s5_loop_filter import (
    S5LoopTransactionFilterJson,
)
from od_search.transaction_filters.json_implementation.s5_loop.s5_loop_n1_loop_filter import (
    S5LoopN1LoopTransactionFilterJson,
)
from od_search.transaction_filters.json_implementation.to_filter import ToTransactionFilterJson


@lru_cache
def get_all_jsonl_transactions_filters() -> (
    dict[JsonTransactionFilterNameFormat, JsonBaseTransactionFilter]
):
    return {
        JsonTransactionFilterNameFormat.TO: ToTransactionFilterJson(),
        JsonTransactionFilterNameFormat.FROM: FromTransactionFilterJson(),
        JsonTransactionFilterNameFormat.N1_LOOP: N1LoopTransactionFilterJson(),
        JsonTransactionFilterNameFormat.N7_LOOP: N7LoopTransactionFilterJson(),
        JsonTransactionFilterNameFormat.BUSINESS_REFERENCE_NUMBER: BusinessInstructionAndReferenceNumbersTransactionFilterJson(),
        JsonTransactionFilterNameFormat.CARRIER_SHIPMENT_STATUS_MESSAGE: BeginningSegmentForTransportationCarrierShipmentStatusMessageTransactionFilterJson(),
        JsonTransactionFilterNameFormat.LX_LOOP: LxLoopTransactionFilterJson(),
        JsonTransactionFilterNameFormat.LX_LOOP_AT7_LOOP: LxLoopAt7LoopTransactionFilterJson(),
        JsonTransactionFilterNameFormat.S5_LOOP: S5LoopTransactionFilterJson(),
        JsonTransactionFilterNameFormat.S5_LOOP_N1_LOOP: S5LoopN1LoopTransactionFilterJson(),
        JsonTransactionFilterNameFormat.S5_LOOP_BUSINESS_REFERENCE_NUMBER: S5LoopBusinessInstructionAndReferenceNumbersTransactionFilterJson(),
        JsonTransactionFilterNameFormat.AT5_LOOP: AT5LoopTransactionFilterJson(),
    }


def get_json_transaction_filter_by_name(
    name: JsonTransactionFilterNameFormat,
) -> JsonBaseTransactionFilter:
    return get_all_jsonl_transactions_filters()[name]
