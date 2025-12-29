# FastAPI Demo 项目

一个基于 FastAPI 和 SQLAlchemy 2.0 的现代化 Web API 项目示例，采用异步架构和分层设计模式。

## 功能特性

- ✅ 基于 FastAPI 的高性能异步 Web 框架
- ✅ SQLAlchemy 2.0 异步 ORM
- ✅ PostgreSQL 数据库支持（使用 asyncpg 驱动）
- ✅ 清晰的分层架构（API → Service → Repository）
- ✅ 自动 API 文档生成（Swagger UI）
- ✅ 环境变量配置管理
- ✅ 数据库自动初始化和迁移

## 技术栈

- **Web 框架**: FastAPI >= 0.128.0
- **数据库**: PostgreSQL (通过 asyncpg)
- **ORM**: SQLAlchemy >= 2.0.45
- **ASGI 服务器**: Uvicorn >= 0.40.0
- **Python 版本**: >= 3.12
- **包管理**: uv

## 项目结构

```
FastAPI_demo/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── test.py       # 测试 API
│   │       └── users.py      # 用户相关 API
│   ├── core/
│   │   ├── config.py         # 配置管理
│   │   └── database.py       # 数据库连接
│   ├── files/                # 静态文件
│   ├── models/
│   │   ├── base.py           # 基础模型
│   │   └── user.py           # 用户模型
│   ├── repositories/
│   │   └── user.py           # 数据访问层
│   ├── services/
│   │   └── user.py           # 业务逻辑层
│   └── main.py               # 应用入口
├── .env                      # 环境变量配置
├── .gitignore
├── pyproject.toml            # 项目配置和依赖
├── README.md
└── uv.lock                   # 依赖锁定文件
```

## 快速开始

### 1. 安装依赖

确保已安装 Python 3.12+ 和 uv 包管理器。

```bash
# 使用 uv 安装依赖
uv sync
```

### 2. 配置环境变量

创建 `.env` 文件（已包含）并配置数据库连接：

```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/database_name
```

### 3. 启动 PostgreSQL 数据库

确保 PostgreSQL 已安装并运行：

```bash
# 使用 Docker 启动 PostgreSQL 数据库
docker run -d \
  --name postgres \
  -e POSTGRES_USER=your_username \
  -e POSTGRES_PASSWORD=your_password \
  -e POSTGRES_DB=your_database \
  -p 5432:5432 \
  postgres:latest
```

### 4. 启动应用

```bash
# 开发模式运行
uv run uvicorn app.main:app --reload

# 或使用 uvicorn 启动
uvicorn app.main:app --reload
```

应用启动后访问：
- API 文档: http://localhost:8000/docs
- ReDoc 文档: http://localhost:8000/redoc

## API 端点

### 用户管理

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | `/v1/users/` | 获取用户列表 |
| POST | `/v1/users/` | 创建新用户 |

### 示例请求

**创建用户**
```bash
curl -X POST "http://localhost:8000/v1/users/?name=张三"
```

**获取用户列表**
```bash
curl -X GET "http://localhost:8000/v1/users/"
```

## 开发指南

### 添加新的 API 端点

1. 在 `app/models/` 中定义数据模型
2. 在 `app/repositories/` 中创建数据访问层
3. 在 `app/services/` 中实现业务逻辑
4. 在 `app/api/v1/` 中创建路由
5. 在 `app/main.py` 中注册路由

### 数据库迁移

项目使用 SQLAlchemy 的声明式模型，应用启动时会自动创建数据库表。

## 环境配置

项目使用 `.env` 文件管理环境变量：

- `DATABASE_URL`: PostgreSQL 数据库连接字符串（必需）

## 分层架构说明

项目采用经典的分层架构：

- **API 层**: 处理 HTTP 请求和响应
- **Service 层**: 实现业务逻辑
- **Repository 层**: 负责数据访问和数据库操作
- **Model 层**: 定义数据模型和数据库表结构

