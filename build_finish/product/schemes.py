from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field, field_validator


class IdSchema(BaseModel):
    id: UUID = Field(
        description="идентификатор объекта",
    )


class BrandCreateSchema(BaseModel):
    title: str = Field(description="название брэнда", min_length=6, max_length=70, examples=["Makita"])
    description: str = Field(description="описание брэнда", default=None)


class BrandSchema(IdSchema):
    title: str = Field(description="название брэнда", examples=["Bosch"])
    description: str = Field(description="описание брэнда", default=None)


class CategoryCreateSchema(BaseModel):
    title: str = Field(description="название категории товара",
                       min_length=3, max_length=70,
                       examples=["Электроинструмент"])
    description: str = Field(description="описание категории товара",
                             default=None,
                             examples=["Ручной инструмент"])


class CategorySchema(IdSchema):
    title: str = Field(description="название категории", examples=["Ручной инструмент"])
    description: str = Field(description="описание категории", default=None, examples=["Ручной инструмент"])


class ProductSchema(IdSchema):
    title: str = Field(description="название товара", min_length=3, max_length=70)
    description: str = Field(description="описание товара", default=None)
    price: float = Field(description="цена товара", gt=0)


class ProductCreateSchema(BaseModel):
    title: str = Field(description="текст вопроса",
                       examples=["Столица Франции?"],
                       max_length=70,
                       min_length=10)
    category_id: UUID = Field(description="идентификатор категории товара")
    brand_id: UUID = Field(description="идентификатор брэнда")
