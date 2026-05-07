import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
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

# ...中间代码略...

if __name__ == "__main__":
    import uvicorn
    # 启动命令：python -m app.main
    uvicorn.run("app.main:app", host="127.0.0.1", port=8001, reload=True)