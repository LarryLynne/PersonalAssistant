class Note:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value