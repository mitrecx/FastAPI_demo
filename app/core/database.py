from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)

# 创建异步会话工厂
# expire_on_commit=False 表示在提交事务后，会话不会过期
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# 定义异步上下文管理器，用于获取数据库会话
# 该上下文管理器会在请求处理开始时创建会话，在处理结束时关闭会话
async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
