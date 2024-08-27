from uuid import UUID

from fastapi import APIRouter

from core.lifespan import brand_accessor
from store.product.base.schemes import query_page, query_page_size
from store.product.brand.schemes import (
    BrandSchema,
    BrandCreateSchema,
    BrandUpdateSchema,
)

brand_route = APIRouter(prefix="/brand", tags=["BRAND"])


@brand_route.post(
    "",
    summary="добавить производителя товара",
    description="Добавить нового производителя для товара.",
    response_model=BrandSchema,
)
async def create_brand(brand: BrandCreateSchema):
    return await brand_accessor.create(**brand.model_dump())


@brand_route.put(
    "/{brand_id}",
    summary="обновить данные производителя",
    description="Обновить данные о производителе.",
    response_model=BrandSchema,
)
async def update_brand(brand_id: UUID, brand: BrandUpdateSchema):
    return await brand_accessor.update(brand_id, **brand.model_dump())


@brand_route.delete(
    "/{brand_id}",
    summary="удалить данные производителя",
    description="Удалить данные производителя.",
    response_model=BrandSchema,
)
async def delete_brand(brand_id: UUID):
    return await brand_accessor.delete(brand_id)


@brand_route.get(
    "",
    summary="получить всех производителей",
    description="Получить всех производителей товаров.",
    response_model=list[BrandSchema],
)
async def get_brands(page: int = query_page, page_size: int = query_page_size):
    return await brand_accessor.get(page, page_size)


@brand_route.get(
    "/{brand_id}",
    summary="получить данные по id.",
    description="получить производителя по id",
    response_model=BrandSchema,
)
async def get_brand_by_id(brand_id: UUID):
    return await brand_accessor.get_by_id(brand_id)
