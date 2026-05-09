import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import chat
from app.api.v1 import oss
from app.common.logger import setup_logging

# 初始化日志配置
setup_logging()

# 初始化FastAPI
app = FastAPI(
    title="Personal Chief API",
    description="私厨",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(chat.router, prefix="/api/v1")
app.include_router(oss.router, prefix="/api/v1")


@app.get("/")
async def serve_index():
    path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    return FileResponse(path)


if __name__ == "__main__":
    import uvicorn
    # 启动命令：python -m app.main
    uvicorn.run("app.main:app", host="127.0.0.1", port=8001, reload=True)