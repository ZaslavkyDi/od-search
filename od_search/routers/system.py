from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/")
async def hello():
    return {"it": "works!"}


@router.get("/healthcheck")
async def healthcheck():
    return {"message": "ok"}
