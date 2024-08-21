from typing import TypedDict
from uuid import UUID

from core.logger import setup_logging
from store.db.postgres_db.accessor import PostgresAccessor
from store.product.models import CategoryModel, BrandModel, ProductModel
from store.product.exceptions import exception_handler


class BrandDict(TypedDict):

    title: str
    is_correct: bool
    question_id: str
    created: str
    modified: str


class ProductAccessor(PostgresAccessor):

    @exception_handler
    async def create_category(self, title: str, description: str) -> CategoryModel:
        category = CategoryModel()
        category.title = title
        category.description = description
        async with self.session as session:
            session.add(category)
            await session.commit()
        return category


    # @exception_handler
    # async def get_question_by_id(self, question_id: str) -> QuestionModel:
    #     smtp = self.get_query_select_by_model(QuestionModel).where(QuestionModel.id == question_id)
    #     question = await self.query_execute(smtp)
    #     return question.scalar_one()
    #
    # @exception_handler
    # async def get_random_question(self, theme_id: str) -> QuestionModel:
    #     smtp = self.get_query_random(QuestionModel).where(QuestionModel.theme_id == theme_id)
    #     question = await self.query_execute(smtp)
    #     return question.scalar_one()
    #
    # @exception_handler
    # async def create_theme(self, title: str) -> ThemeModel:
    #     theme = ThemeModel()
    #     theme.title = title
    #     async with self.session as session:
    #         session.add(theme)
    #         await session.commit()
    #     return theme
    #
    # @exception_handler
    # async def get_theme_by_id(self, theme_id: str) -> ThemeModel:
    #     smtp = self.get_query_select_by_model(ThemeModel).where(ThemeModel.id == theme_id)
    #     theme = await self.query_execute(smtp)
    #     return theme.scalar_one()
    #
    # @exception_handler
    # async def get_themes(self) -> list[ThemeModel]:
    #     smtp = self.get_query_select_by_fields(ThemeModel.id, ThemeModel.title)
    #     result = await self.query_execute(smtp)
    #     return await self._result_to_theme_model(result)
    #
    # async def get_themes_with_questions(self):
    #     smtp = (self.get_query_select_by_fields(ThemeModel.id, ThemeModel.title)
    #             .join(QuestionModel, QuestionModel.theme_id == ThemeModel.id)
    #             .distinct())
    #     result = await self.query_execute(smtp)
    #     return await self._result_to_theme_model(result)
    #
    # @staticmethod
    # async def _result_to_theme_model(result) -> list[ThemeModel]:
    #     themes = []
    #     for data in result.mappings().all():
    #         theme = ThemeModel()
    #         theme.id = data["id"]
    #         theme.title = data["title"]
    #         themes.append(theme)
    #     return themes


product_accessor = ProductAccessor(setup_logging())
