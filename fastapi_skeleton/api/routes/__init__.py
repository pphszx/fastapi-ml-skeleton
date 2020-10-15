from fastapi import APIRouter

from fastapi_skeleton.api.routes import heartbeat, houseprice, iris, haier

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["健康检测"], prefix="/health")
api_router.include_router(haier.router, tags=["海尔模型"], prefix="/model")
api_router.include_router(houseprice.router, tags=["加州房价模型"], prefix="/model")
api_router.include_router(iris.router, tags=["莺尾花模型"], prefix="/model")
