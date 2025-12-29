from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.services.user import UserService

router = APIRouter(prefix="/v1/users", tags=["users"])


@router.get("/")
async def list_users(session: AsyncSession = Depends(get_session)):
    service = UserService(session)
    return await service.list_users()


@router.post("/")
async def create_user(name: str, session: AsyncSession = Depends(get_session)):
    service = UserService(session)
    return await service.create_user(name)
