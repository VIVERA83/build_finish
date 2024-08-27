from dataclasses import dataclass
from datetime import datetime
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey, text, DATETIME, func
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP

from store.db.postgres_db.accessor import Base


@dataclass
class BaseModel:
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    created: Mapped[DATETIME] = mapped_column(
        TIMESTAMP,
        default=datetime.now(),
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

    modified: Mapped[DATETIME] = mapped_column(
        TIMESTAMP,
        default=datetime.now(),
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

    def __repr__(self):
        return "{class_name}(id={id})".format(
            id=self.id,
            class_name=self.__class__.__name__,
        )

    __str__ = __repr__


@dataclass
class CategoryModel(Base, BaseModel):
    __tablename__ = "categories"

    title: Mapped[str] = mapped_column(unique=True)
    products: Mapped[List["ProductModel"]] = relationship(
        "ProductModel", lazy="selectin", cascade="delete"
    )
    description: Mapped[str] = mapped_column(server_default="Описание категории.")


@dataclass
class BrandModel(Base, BaseModel):
    __tablename__ = "brands"

    title: Mapped[str] = mapped_column(unique=True)
    products: Mapped[List["ProductModel"]] = relationship(
        "ProductModel", lazy="selectin", cascade="delete"
    )
    description: Mapped[str] = mapped_column(server_default="Описание производителя.")


@dataclass
class ProductModel(Base, BaseModel):
    __tablename__ = "products"

    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(server_default="Описание товара.")
    price: Mapped[float] = mapped_column(nullable=False)

    category: Mapped[UUID] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE"), nullable=False, index=True
    )
    brand: Mapped[UUID] = mapped_column(
        ForeignKey("brands.id", ondelete="CASCADE"), nullable=False, index=True
    )
