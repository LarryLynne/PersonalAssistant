from Field import Field
import re

class Phone(Field):
    def __init__(self, value: str) -> None:
        if value:
            ph = re.findall(r"[0-9]", value)
            ph = ''.join(ph)
            if len(ph) == 12:
                self.value = (str(value))
            else:
                raise ValueError("Incorrect phone number")
        else:
            self.value = (str(value))

    def __str__(self) -> str:
        return str(self.value)




