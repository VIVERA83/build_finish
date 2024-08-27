from uuid import UUID

from store.product.base.accessor import BaseAccessor
from store.product.base.exceptions import exception_handler
from store.product.category.exceptions import (
    CategoryDuplicateException,
    CategoryNotFoundException,
)
from store.product.models import CategoryModel


class CategoryAccessor(BaseAccessor):

    @exception_handler(CategoryNotFoundException)
    async def get_by_id(self, category_id: UUID) -> CategoryModel:
        smtp = self.db.get_query_select_by_fields(
            CategoryModel.id, CategoryModel.title, CategoryModel.description
        ).where(CategoryModel.id == category_id)
        result = await self.db.query_execute(smtp)
        return CategoryModel(**result.mappings().one())

    @exception_handler()
    async def get(self, page: int = 1, limit: int = 10) -> list[CategoryModel]:
        smtp = (
            self.db.get_query_select_by_model(CategoryModel)
            .limit(limit)
            .offset((page - 1) * limit)
        )
        result = await self.db.query_execute(smtp)
        return result.scalars().all()  # type: ignore

    @exception_handler(duplicate=CategoryDuplicateException)
    async def create(self, title: str, description: str) -> CategoryModel:
        brand = CategoryModel(title=title, description=description)  # type: ignore
        async with self.db.session as session:
            session.add(brand)
            await session.commit()
        return brand

    @exception_handler(CategoryNotFoundException)
    async def update(
        self, brand_id: UUID, title: str = None, description: str = None
    ) -> CategoryModel:
        update_data = {
            key: value
            for key, value in {"title": title, "description": description}.items()
            if value is not None
        }
        smtp = (
            self.db.get_query_update(CategoryModel, **update_data)
            .where(CategoryModel.id == brand_id)
            .returning(CategoryModel.id, CategoryModel.title, CategoryModel.description)
        )
        async with self.db.session as session:
            result = await session.execute(smtp)
            await session.commit()
            return CategoryModel(**result.mappings().one())

    @exception_handler(CategoryNotFoundException)
    async def delete(self, brand_id: UUID) -> CategoryModel:
        smtp = (
            self.db.get_query_delete(CategoryModel)
            .where(CategoryModel.id == brand_id)
            .returning(CategoryModel.id, CategoryModel.title, CategoryModel.description)
        )
        result = await self.db.query_execute(smtp)
        return CategoryModel(**result.mappings().one())
