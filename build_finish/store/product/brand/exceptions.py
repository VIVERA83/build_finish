from store.product.base.exceptions import ExceptionBase


class BrandNotFoundException(ExceptionBase):
    args = ("Производитель не найден.",)
    code = 404


class BrandDuplicateException(ExceptionBase):
    args = ("Повторяющиеся значения в таблице производителей.",)
    code = 400
