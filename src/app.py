from fastapi import FastAPI
from contextlib import asynccontextmanager


from src.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="Backend Telegram Bot VKS",
    description="",
    debug=settings.debug,
)
