from pydantic import BaseModel, Field

from store.product.base.schemes import IdSchema


class BrandSchema(IdSchema):
    title: str = Field(description="название брэнда", examples=["Bosch"])
    description: str = Field(description="описание брэнда", default=None)


class BrandCreateSchema(BaseModel):
    title: str = Field(
        description="название брэнда", min_length=3, max_length=70, examples=["Makita"]
    )
    description: str = Field(description="описание брэнда", default=None)


class BrandUpdateSchema(BaseModel):
    title: str = Field(
        description="название брэнда",
        min_length=3,
        max_length=70,
        examples=["Makita"],
        default=None,
    )
    description: str = Field(description="описание брэнда", default=None)
