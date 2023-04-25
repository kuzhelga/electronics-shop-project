from src.phone import Phone


def test__repr__():
    """Тест метода вывода для разработчика"""
    phone = Phone("Nokia", 35000, 10, 2)
    assert repr(phone) == "Phone('Nokia', 35000, 10, 2)"


def test_number_of_sim():
    """Тест сеттера для кол-ва сим-карт"""
    phone2 = Phone("Nokia", 35000, 10, 5)
    assert phone2.number_of_sim == 5
    phone2.number_of_sim = 3
    assert phone2.number_of_sim == 3
    # Для проверки раскомментировать
    # phone2.number_of_sim = 0
