from uuid import UUID

from pydantic import Field, BaseModel

from fastapi import Query
from store.product.base.schemes import IdSchema


class ProductSchema(IdSchema):
    title: str = Field(description="название товара", min_length=3, max_length=70)
    description: str = Field(description="описание товара", default=None)
    price: float = Field(description="цена товара", gt=0)
    brand: UUID = Field(description="идентификатор брэнда")
    category: UUID = Field(description="идентификатор категории товара")


class ProductCreateSchema(BaseModel):
    title: str = Field(
        description="Название товара",
        examples=["Электро рубанок"],
        max_length=70,
        min_length=3,
    )
    price: float = Field(description="цена товара", gt=0)
    category: UUID = Field(description="идентификатор категории товара")
    brand: UUID = Field(description="идентификатор брэнда")
    description: str = Field(
        description="описание товара", default=None, examples=["Красный"]
    )


class ProductUpdateSchema(BaseModel):
    title: str = Field(
        description="название товара.",
        min_length=3,
        max_length=70,
        examples=["Киянка."],
        default=None,
    )
    description: str = Field(description="описание товара", default=None)
    price: float = Field(description="цена товара", gt=1, default=None)
    category: UUID = Field(description="идентификатор категории товара", default=None)
    brand: UUID = Field(description="идентификатор брэнда", default=None)


query_brand = Query(
    default=None,
    description="идентификатор производителя",
)

query_category = Query(
    default=None,
    description="идентификатор категории",
)
