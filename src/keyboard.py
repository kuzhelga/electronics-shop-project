from src.item import Item


class MixinLog:
    """Класс для смены языка клавиатуры"""
    __language = "EN"

    def __init__(self, *args):
        super().__init__(*args)

    @property
    def language(self):
        """Сеттер для раскладки языка"""
        return self.__language

    def change_lang(self):
        """Метод для смены раскладки клавиатуры"""
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"

        return self


class KeyBoard(Item, MixinLog):
    """Класс для товара Клавиатура"""

    def __init__(self, *args):
        super().__init__(*args)
