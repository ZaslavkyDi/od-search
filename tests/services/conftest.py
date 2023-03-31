import httpx
import pytest

from od_search.common.httpx_connection import get_httpx_client, close_httpx_client
from od_search.common.orderful_api_handler import OrderfulApiHandler
from od_search.services.orderful_transaction_service import OrderfulTransactionService


@pytest.fixture(scope="session")
async def httpx_client_fixture() -> httpx.AsyncClient:
    client = get_httpx_client()
    yield client
    await close_httpx_client()


@pytest.fixture
def orderful_api_handler(httpx_client_fixture: httpx.AsyncClient) -> OrderfulApiHandler:
    yield OrderfulApiHandler(httpx_client=httpx_client_fixture)


@pytest.fixture
def orderful_transaction_service(
    orderful_api_handler: OrderfulApiHandler,
) -> OrderfulTransactionService:
    yield OrderfulTransactionService(api_handler=orderful_api_handler)
