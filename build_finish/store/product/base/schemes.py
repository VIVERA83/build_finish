from uuid import UUID

from fastapi import Query
from pydantic import BaseModel, Field


class IdSchema(BaseModel):
    id: UUID = Field(
        description="идентификатор объекта",
    )


query_page = Query(
    default=1,
    description="номер страницы для получения результатов",
    ge=1,
)

query_page_size = Query(
    default=10,
    description="количество результатов на странице",
    ge=1,
)
