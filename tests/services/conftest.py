import pytest

from app.services.api_handlers.orderful_api_handler import OrderfulApiHandler
from app.services.orderful_transaction_service import OrderfulTransactionService


@pytest.fixture
def orderful_api_handler() -> OrderfulApiHandler:
    yield OrderfulApiHandler()


@pytest.fixture
def orderful_transaction_service(orderful_api_handler: OrderfulApiHandler) -> OrderfulTransactionService:
    yield OrderfulTransactionService(api_handler=orderful_api_handler)
