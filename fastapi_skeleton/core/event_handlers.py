import os
from typing import Callable

from fastapi import FastAPI
from loguru import logger

from fastapi_skeleton.core.config import DEFAULT_MODEL_PATH
from fastapi_skeleton.model import dct_model


def _startup_model(app: FastAPI) -> None:
    models = {}
    with os.scandir(DEFAULT_MODEL_PATH) as entries:
        for entry in entries:
            if entry.is_dir():
                try:
                    f = os.path.join(entry.path, "model.joblib")
                    models[entry.name.lower()] = dct_model[entry.name.lower()](
                        f
                    )
                except FileNotFoundError:
                    logger.warning(f"{f} not exists")
    app.state.model = models


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        _startup_model(app)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)

    return shutdown
