class Ship(object):
    def __init__(self, name: str, length: int) -> None:
        super().__init__()
        self.name = name
        self.length = length
        self.health = length

    def __str__(self) -> str:
        return self.name
