import httpx

HTTPX_ASYNC_CLIENT: httpx.AsyncClient | None = None


def init_httpx_client() -> None:
    global HTTPX_ASYNC_CLIENT
    HTTPX_ASYNC_CLIENT = httpx.AsyncClient()


async def close_httpx_client() -> None:
    global HTTPX_ASYNC_CLIENT
    if HTTPX_ASYNC_CLIENT:
        await HTTPX_ASYNC_CLIENT.aclose()
        HTTPX_ASYNC_CLIENT = None


def get_httpx_client() -> httpx.AsyncClient:
    global HTTPX_ASYNC_CLIENT
    if not HTTPX_ASYNC_CLIENT:
        init_httpx_client()

    return HTTPX_ASYNC_CLIENT
