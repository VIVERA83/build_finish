from uuid import UUID

from fastapi import APIRouter

from core.lifespan import product_accessor
from store.product.base.schemes import query_page_size, query_page
from store.product.product.schemes import (
    ProductSchema,
    ProductCreateSchema,
    ProductUpdateSchema,
    query_brand,
    query_category,
)

product_route = APIRouter(prefix="/product", tags=["PRODUCT"])


@product_route.post(
    "",
    summary="добавить товар",
    description="Добавить новый товар.",
    response_model=ProductSchema,
)
async def create_product(product: ProductCreateSchema):
    return await product_accessor.create(**product.model_dump())


@product_route.get(
    "",
    summary="получить товары",
    description="Получить товары согласно заданным критериям отбора.",
    response_model=list[ProductSchema],
)
async def get_category(
    page: int = query_page,
    page_size: int = query_page_size,
    brand: UUID = query_brand,
    category: UUID = query_category,
):
    return await product_accessor.get(page, page_size, brand, category)


@product_route.get(
    "/{product_id}",
    summary="получить данные по id.",
    description="получить товар по id",
    response_model=ProductSchema,
)
async def get_brand_by_id(product_id: UUID):
    return await product_accessor.get_by_id(product_id)


@product_route.delete(
    "/{product_id}",
    summary="удалить товар",
    description="Удалить товар по id.",
    response_model=ProductSchema,
)
async def delete_brand(product_id: UUID):
    return await product_accessor.delete(product_id)


@product_route.put(
    "/{product_id}",
    summary="изменить товар",
    description="Обновить данные о товаре.",
    response_model=ProductSchema,
)
async def update_brand(product_id: UUID, product: ProductUpdateSchema):
    return await product_accessor.update(product_id, **product.model_dump())
