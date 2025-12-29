from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user import UserRepository

class UserService:
    def __init__(self, session: AsyncSession):
        self.repo = UserRepository(session)

    async def list_users(self):
        return await self.repo.list_users()

    async def create_user(self, name: str):
        return await self.repo.create_user(name)