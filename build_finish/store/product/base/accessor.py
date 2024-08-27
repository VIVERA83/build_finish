from logging import Logger

from store.db.postgres_db.accessor import PostgresAccessor


class BaseAccessor:
    def __init__(self, db: PostgresAccessor, logger: Logger):
        self.db = db
        self.logger = logger
        self.logger.info(f"{self.__class__.__name__} инициализирован.")
