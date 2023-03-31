from contextlib import asynccontextmanager
from typing import AsyncContextManager

import uvicorn
from fastapi import FastAPI

from od_search.common.httpx_connection import init_httpx_client, close_httpx_client
from od_search.config import get_app_settings
from od_search.routers import od_search, system


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI) -> AsyncContextManager[None] | FastAPI:
    # on startup
    init_httpx_client()
    yield
    # in shutdown
    await close_httpx_client()


app = FastAPI(lifespan=lifespan)

app.include_router(od_search.router)
app.include_router(system.router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=get_app_settings().host,
        port=8880,
        reload=False,
    )
