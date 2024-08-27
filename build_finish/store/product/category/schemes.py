from pydantic import BaseModel, Field

from store.product.base.schemes import IdSchema


class CategoryCreateSchema(BaseModel):
    title: str = Field(
        description="название категории товара",
        min_length=3,
        max_length=70,
        examples=["Электроинструмент"],
    )
    description: str = Field(
        description="описание категории товара",
        default=None,
        examples=["Ручной инструмент"],
    )


class CategorySchema(IdSchema):
    title: str = Field(description="название категории", examples=["Ручной инструмент"])
    description: str = Field(
        description="описание категории", default=None, examples=["Ручной инструмент"]
    )


class CategoryUpdateSchema(BaseModel):
    title: str = Field(
        description="название категории",
        min_length=3,
        max_length=70,
        examples=["Инструмент"],
        default=None,
    )
    description: str = Field(description="описание категории", default=None)
