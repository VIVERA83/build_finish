from functools import wraps

from sqlalchemy.exc import NoResultFound


class ExceptionBase(Exception):
    """Базовый класс для всех исключений."""

    args = ("Неизвестное исключение.",)
    exception = None
    code = 500

    def __init__(self, *args, code: int = None, exception: Exception = None):

        if args:
            self.args = args
        if exception:
            self.exception = exception
        if code:
            self.code = code

    def __str__(self):
        return f"Исключение: {self.args[0]}, код: {self.code}"


def __str__(self):
    return f"Параметры исключения: {self.args[0]}"


class DataBaseConnectionException(ExceptionBase):
    args = ("Ошибка подключения к базе данных. Попробуйте позже.",)


class DataBaseUnknownException(ExceptionBase):
    args = ("Неизвестная ошибка базы данных.",)


class OperationNotFoundException(ExceptionBase):
    args = ("Transaction not found.",)
    code = 404


class ThemeNotFound(ExceptionBase):
    args = ("Тема не найдена.",)
    code = 404


class DuplicateException(ExceptionBase):
    args = ("Повторяющие значение в таблице. Придумайте другое значение.",)
    code = 400


def exception_handler(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        try:
            return await func(self, *args, **kwargs)
        except NoResultFound as e:
            raise OperationNotFoundException(exception=e)
        except IOError as e:
            if e.errno == 111:
                raise DataBaseConnectionException(exception=e)
        except Exception as e:
            self.logger.warning(str(e))
            if orig := getattr(e, "orig", None):
                pg_code = getattr(orig, "pgcode", None)
                self.logger.error(f"{pg_code=}")
                if pg_code and pg_code == "23505":
                    message = pg_code_handler(e,"already exists.", ", такая запись уже существует.")
                    raise DuplicateException(message, exception=e)
                elif pg_code and pg_code == "23503":
                    message = pg_code_handler(e,'is not present in table "brands".', ", такой  записи не существует.")
                    raise ThemeNotFound(message, exception=e)

            raise DataBaseUnknownException(exception=e)

        raise DataBaseUnknownException()

    return wrapper


def pg_code_handler(e: Exception, replace: str, insert: str) -> str:
    message = e.args[0].split("Key ")[-1].replace("(", "").replace(")", "").replace("=", " : ")
    message = message.replace(replace, insert)
    return message
