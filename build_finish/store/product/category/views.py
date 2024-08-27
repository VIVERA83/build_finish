from uuid import UUID

from fastapi import APIRouter

from core.lifespan import category_accessor
from store.product.base.schemes import query_page, query_page_size
from store.product.category.schemes import (
    CategorySchema,
    CategoryCreateSchema,
    CategoryUpdateSchema,
)

category_route = APIRouter(prefix="/category", tags=["CATEGORY"])


@category_route.post(
    "",
    summary="добавить категорию товара",
    description="Добавить новую категорию товара.",
    response_model=CategorySchema,
)
async def create_brand(category: CategoryCreateSchema):
    return await category_accessor.create(**category.model_dump())


@category_route.put(
    "/{brand_id}",
    summary="обновить категорию",
    description="Обновить данные о категории товара.",
    response_model=CategorySchema,
)
async def update_brand(category_id: UUID, category: CategoryUpdateSchema):
    return await category_accessor.update(category_id, **category.model_dump())


@category_route.delete(
    "/{brand_id}",
    summary="удалить категорию",
    description="Удалить категорию товара.",
    response_model=CategorySchema,
)
async def delete_brand(category_id: UUID):
    return await category_accessor.delete(category_id)


@category_route.get(
    "",
    summary="получить все категории",
    description="Получить категории товаров.",
    response_model=list[CategorySchema],
)
async def get_brands(page: int = query_page, page_size: int = query_page_size):
    return await category_accessor.get(page, page_size)


@category_route.get(
    "/{brand_id}",
    summary="получить данные по id.",
    description="получить категорию по id",
    response_model=CategorySchema,
)
async def get_brand_by_id(category_id: UUID):
    return await category_accessor.get_by_id(category_id)
