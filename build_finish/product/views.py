from fastapi import APIRouter

from product.schemes import ProductCreateSchema, ProductSchema, BrandCreateSchema, CategorySchema, CategoryCreateSchema
from store.product.accessor import product_accessor

category_route = APIRouter(prefix="/category", tags=["CATEGORY"])
brand_route = APIRouter(prefix="/brand", tags=["BRAND"])


@category_route.post(
    "",
    summary="добавить категорию товара",
    description="Добавить новую категорию для товара.",
    response_model=CategorySchema,
)
async def create_category(category: CategoryCreateSchema):
    return await product_accessor.create_category(**category.model_dump())
