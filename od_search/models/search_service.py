from pydantic.dataclasses import dataclass


@dataclass
class TransactionPageRange:
    start_page_number: int
    end_page_number: int
