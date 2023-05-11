from src.item import Item


class MixinLog:
    """Класс для смены языка клавиатуры"""
    def __init__(self):
        self.__language == "EN"

    @property
    def language(self):
        """Сеттер для раскладки языка"""
        return self.__language

    def change_lang(self):
        """Метод для смены раскладки клавиатуры"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

class KeyBoard(Item, MixinLog):
    """Класс для товара Клавиатура"""

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

