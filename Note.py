class Note():
    def __init__(self, caption: str) -> None:
        self.caption = caption
        self.text = None

    def __str__(self) -> str:
        return f"{self.caption} : {self.text}"
