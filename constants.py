from enum import Enum


class TransactionDirection(Enum):
    OUT = "out"
    IN = "in"


class TransactionTypeId(Enum):
    TYPE_204_ID = 18
    TYPE_210_ID = 19
    TYPE_214_ID = 20
    TYPE_990_ID = 34
