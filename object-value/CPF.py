import re

class InvalidCPFError(ValueError):
    pass

class CPF:
    _CPF_REGEX = re.compile(r'^(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$')

    def __init__(self, cpf: str):
        if not self._CPF_REGEX.match(cpf):
            raise InvalidCPFError(f"Formato de CPF inválido: {cpf}")
        
        self._value = re.sub(r'\D', '', cpf)

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other):
        return isinstance(other, CPF) and self._value == other._value

    def __str__(self):
        # Retorna formatado: 123.456.789-00
        return f"{self._value[:3]}.{self._value[3:6]}.{self._value[6:9]}-{self._value[9:]}"
