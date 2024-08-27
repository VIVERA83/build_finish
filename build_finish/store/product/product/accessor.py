from uuid import UUID

from store.product.base.accessor import BaseAccessor
from store.product.base.exceptions import exception_handler
from store.product.models import ProductModel
from store.product.product.exceptions import (
    ProductForeignKeyException,
    ProductNotFoundException,
)


class ProductAccessor(BaseAccessor):

    @exception_handler()
    async def get_by_id(self, product_id: UUID) -> ProductModel:
        smtp = self.db.get_query_select_by_model(ProductModel).where(
            ProductModel.id == product_id
        )
        result = await self.db.query_execute(smtp)
        return result.scalars().one()  # type: ignore

    @exception_handler()
    async def get(
        self, page: int, limit: int, brand: UUID = None, category: UUID = None
    ) -> list[ProductModel]:
        smtp = (
            self.db.get_query_select_by_model(ProductModel)
            .limit(limit)
            .offset((page - 1) * limit)
            .where()
        )
        if brand:
            smtp = smtp.where(ProductModel.brand == brand)
        if category:
            smtp = smtp.where(ProductModel.category == category)
        result = await self.db.query_execute(smtp)
        return result.scalars().all()  # type: ignore

    @exception_handler(foreign_key=ProductForeignKeyException)
    async def create(
        self, title: str, price: float, category: UUID, brand: UUID, description: str
    ) -> ProductModel:
        brand = ProductModel(
            title=title,
            description=description,
            price=price,
            category=category,  # type: ignore
            brand=brand,
        )  # type: ignore
        async with self.db.session as session:
            session.add(brand)
            await session.commit()
        return brand

    @exception_handler(
        not_found=ProductNotFoundException, foreign_key=ProductForeignKeyException
    )
    async def update(
        self,
        product_id: UUID,
        title: str = None,
        description: str = None,
        price: float = None,
        category: UUID = None,
        brand: UUID = None,
    ) -> ProductModel:
        update_data = {
            key: value
            for key, value in locals().items()
            if value and key not in ["self", "product_id"]
        }
        smtp = (
            self.db.get_query_update(ProductModel, **update_data)
            .where(ProductModel.id == product_id)
            .returning(ProductModel)
        )
        async with self.db.session as session:
            product = await session.execute(smtp)
            return product.scalars().one()

    @exception_handler(not_found=ProductNotFoundException)
    async def delete(self, product_id: UUID) -> ProductModel:
        smtp = (
            self.db.get_query_delete(ProductModel)
            .where(ProductModel.id == product_id)
            .returning(ProductModel)
        )
        product = await self.db.query_execute(smtp)
        return product.scalars().one()
