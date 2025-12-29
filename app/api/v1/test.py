from fastapi import APIRouter, Path, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal
from fastapi.responses import HTMLResponse, FileResponse

router = APIRouter(prefix="/v1/test", tags=["test"])


# app 是 FastAPI 应用实例，用于定义路由和处理请求
# @app.get("/") 定义了一个 GET 请求的路由，路径为 "/"
# 当客户端访问 "/" 时，会调用 root 函数并返回 {"message": "Hello FastAPI with uv"}
@router.get("/")
def root():
    return {"message": "Hello FastAPI with uv"}


# 路径参数, 可以用于 get, post, put, delete 等请求
@router.get("/hello/{name}")
async def hello_name(name: str = Path(..., description="要打招呼的姓名")):
    return {"message": f"Hello, {name}"}


# 查询参数, 只能用于 get 请求
@router.get("/news/news_list")
async def news_list(
    skip: int = Query(0, lt=100, description="跳过的新闻数量"),
    limit: int = Query(10, le=100, description="返回的新闻数量"),
):
    return {"skip": skip, "limit": limit}


class User(BaseModel):
    username: str = Field(default="张三", description="用户名")
    password: str = Field(..., min_length=6, max_length=10, description="密码")


# 请求体参数, 只能用于 post, put 请求
@router.post("/register")
async def register(user: User):
    return {"username": user.username}


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


# 查询参数
@router.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query


@router.get("/items/2", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """


# 返回文件
@router.get("/file")
async def read_file():
    path = "app/files/1.jpg"
    return FileResponse(path)
