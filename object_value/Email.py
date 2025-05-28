import re

class InvalidEmailError(ValueError):
    pass

class Email:
    EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

    def __init__(self, address: str):
        if not self.EMAIL_REGEX.match(address):
            raise InvalidEmailError(f"Email inválido: {address}")
        self.__value = address

    @property
    def value(self) -> str:
        return self.__value

    def __eq__(self, other):
        return isinstance(other, Email) and self.__value == other.__value

    def __str__(self):
        return self.__value
