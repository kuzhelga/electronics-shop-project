from src.item import Item


class Phone(Item):
    """Содержит все атрибуты класса Item и дополнительно атрибут, содержащий количество поддерживаемых сим-карт"""

    def __init__(self, name, price, quantity, number_of_sim):
        """Расширение класса Item"""
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """Метод вывода для разработчиков"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        """Метод для сложения экземпляров класса"""
        return int(self.quantity) + int(other.quantity)
