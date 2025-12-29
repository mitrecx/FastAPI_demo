from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.v1.users import router as user_router
from app.api.v1.test import router as test_router
from app.models.base import Base
from app.core.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    # shutdown
    await engine.dispose()


app = FastAPI(
    title="你好 FastAPI SQLAlchemy 2.0",
    lifespan=lifespan,
)

app.include_router(user_router)
app.include_router(test_router)
