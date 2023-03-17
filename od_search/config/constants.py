from enum import Enum


class TransactionDirection(Enum):
    OUT = "out"
    IN = "in"


class TransactionTypeId(Enum):
    TYPE_204_ID = 18
    TYPE_210_ID = 19
    TYPE_214_ID = 20
    TYPE_990_ID = 34


class TransactionFilterName(Enum):
    TO = "to"
    FROM = "from"
    N1_LOOP = "n1_loop"
    N7_LOOP = "n7_loop"
    BUSINESS_REFERENCE_NUMBER = "business_instruction_and_reference_numbers"
    CARRIER_SHIPMENT_STATUS_MESSAGE = (
        "beginning_segment_for_transportation_carrier_shipment_status_message"
    )
    LX_LOOP = "lx_loop"
    LX_LOOP_AT7_LOOP = "lx_loop.at7_loop"
    S5_LOOP = "s5_loop"
    S5_LOOP_N1_LOOP = "s5_loop.n1_loop"
    S5_LOOP_BUSINESS_REFERENCE_NUMBER = "s5_loop.business_instruction_and_reference_numbers"
