from store.product.base.exceptions import ExceptionBase


class CategoryNotFoundException(ExceptionBase):
    args = ("Категория не найдена.",)
    code = 404


class CategoryDuplicateException(ExceptionBase):
    args = ("Повторяющиеся значения в таблице категорий.",)
    code = 400
