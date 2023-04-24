import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        """Метод вывода для разработчиков"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Метод вывода для пользователей"""
        return f'{self.__name}'

    @property
    def name(self):
        """Геттер для name - возвращает название товара"""
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            print("Длина наименования товара больше 10 символов")
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file="../src/items.csv") -> None:
        """Класс-метод, инициализирующий экземпляры класса данными из файла"""
        cls.all = []
        with open(file, encoding="cp1251") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string):
        """Статический метод, возвращающий число из числа-строки"""
        return int(float(string)) if "." in string else int(string)

    def __add__(self, other):
        """Метод для сложения экземпляров класса Item и подклассов"""
        if not isinstance(self, Item) and not isinstance(other, Item):
            raise Exception("Складывать можно только объекты класса Item и Phone!")

        return self.quantity + other.quantity
