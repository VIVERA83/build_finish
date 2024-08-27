from store.product.base.exceptions import ExceptionBase


class ProductNotFoundException(ExceptionBase):
    args = ("Товар не найден.",)
    code = 404


class ProductDuplicateException(ExceptionBase):
    args = ("Повторяющие значение в таблице Товаров.",)
    code = 400


class ProductForeignKeyException(ExceptionBase):
    args = ("Не верно указана связь с одной из таблиц : Категории, Производитель",)
    code = 400
