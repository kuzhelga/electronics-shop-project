from src.item import Item


class Phone(Item):
    """Содержит все атрибуты класса Item и дополнительно атрибут, содержащий количество поддерживаемых сим-карт"""

    def __init__(self, name, price, quantity, number_of_sim):
        """Расширение класса Item"""
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Метод вывода для разработчиков"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")

        else:
            self.__number_of_sim = value
