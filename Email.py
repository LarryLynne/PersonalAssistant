from Field import Field
import re
from messages import messages

class Email(Field):
    def __init__(self, value: str) -> None:
        self._value = None
        self.value = value

    def value(self, value):
        if value:
            ph = re.findall(r"[A-z]+[.]*[\w]*[.]*[\w]+[@][a-z]+[.][a-z]{2,10}", value)
            if ph:
                self._value = (str(value))
            else:
                raise ValueError(messages.get(23))
        else:
            self._value = (str(value))

    def __str__(self) -> str:
        return str(self._value)