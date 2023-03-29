import uvicorn
from fastapi import FastAPI

from od_search.config import get_app_settings
from od_search.routers import od_search, system

app = FastAPI()

app.include_router(od_search.router)
app.include_router(system.router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=get_app_settings().host,
        port=8880,
        reload=False,
    )
