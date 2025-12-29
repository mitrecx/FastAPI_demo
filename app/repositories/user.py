from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list_users(self) -> list[User]:
        result = await self.session.execute(select(User))
        return result.scalars().all()

    async def create_user(self, name: str) -> User:
        user = User(name=name)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
