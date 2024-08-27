from uuid import UUID

from store.product.base.accessor import BaseAccessor
from store.product.base.exceptions import exception_handler
from store.product.brand.exceptions import (
    BrandNotFoundException,
    BrandDuplicateException,
)

from store.product.models import BrandModel


class BrandAccessor(BaseAccessor):

    @exception_handler(BrandNotFoundException)
    async def get_by_id(self, brand_id: UUID) -> BrandModel:
        smtp = self.db.get_query_select_by_fields(
            BrandModel.id, BrandModel.title, BrandModel.description
        ).where(BrandModel.id == brand_id)
        result = await self.db.query_execute(smtp)
        return BrandModel(**result.mappings().one())

    @exception_handler()
    async def get(self, page: int = 1, limit: int = 10) -> list[BrandModel]:
        smtp = (
            self.db.get_query_select_by_model(BrandModel)
            .limit(limit)
            .offset((page - 1) * limit)
        )
        result = await self.db.query_execute(smtp)
        return result.scalars().all()  # type: ignore

    @exception_handler(duplicate=BrandDuplicateException)
    async def create(self, title: str, description: str) -> BrandModel:
        brand = BrandModel(title=title, description=description)  # type: ignore
        async with self.db.session as session:
            session.add(brand)
            await session.commit()
        return brand

    @exception_handler(BrandNotFoundException)
    async def update(
        self, brand_id: UUID, title: str = None, description: str = None
    ) -> BrandModel:
        update_data = {
            key: value
            for key, value in {"title": title, "description": description}.items()
            if value is not None
        }
        smtp = (
            self.db.get_query_update(BrandModel, **update_data)
            .where(BrandModel.id == brand_id)
            .returning(BrandModel.id, BrandModel.title, BrandModel.description)
        )
        async with self.db.session as session:
            result = await session.execute(smtp)
            await session.commit()
            return BrandModel(**result.mappings().one())

    @exception_handler(BrandNotFoundException)
    async def delete(self, brand_id: UUID) -> BrandModel:
        smtp = (
            self.db.get_query_delete(BrandModel)
            .where(BrandModel.id == brand_id)
            .returning(BrandModel.id, BrandModel.title, BrandModel.description)
        )
        result = await self.db.query_execute(smtp)
        return BrandModel(**result.mappings().one())
