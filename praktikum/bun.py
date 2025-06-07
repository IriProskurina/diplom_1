class Bun:
    """
    Модель булочки для бургера.
    Булочке можно дать название и назначить цену, а также изменить их после создания.
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def set_name(self, name: str):
        """Установить новое имя булочки."""
        self.name = name

    def set_price(self, price: float):
        """Установить новую цену булочки."""
        self.price = price
