"""Модуль сборки приложения."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.logger import setup_logging
from core.middelware import setup_middleware
from core.routes import setup_routes
from core.app import Application
from core.settings import AppSettings
from store.product.accessor import product_accessor


@asynccontextmanager
async def lifespan(_: FastAPI):
    await product_accessor.connect()
    yield
    await product_accessor.disconnect()
    ...


def setup_app() -> "Application":
    """Создание и настройка основного FastAPI приложения.

    Returns:
        Application: Основное FastAPI приложение.
    """
    settings = AppSettings()
    app = Application(
        lifespan=lifespan,
        version=settings.version,
        title=settings.title,
        description=settings.description,
    )
    app.logger = setup_logging()
    setup_middleware(app)
    setup_routes(app)
    return app
