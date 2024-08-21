import logging

from core.settings import AppSettings
from fastapi import FastAPI
from fastapi import Request as FastAPIRequest


class Application(FastAPI):
    """Основной класс приложения.

    Этот класс отвечает за инициализацию приложения Fast API,
    а также за управление зависимостями и конфигурацией приложения.

    Attributes:
        logger (logging.Logger): Экземпляр логгера.
        docs_url (str): URL-адрес документации.
    """

    logger: logging.Logger
    docs_url: str
