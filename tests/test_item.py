"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def data():
    """Экземпляр для теста"""
    return Item("Laptop", 50000, 2)


def test_calculate_total_price(data):
    """Тест для проверки функции расчета стоимости товара"""
    assert data.calculate_total_price() == 100000


def test_apply_discount(data):
    """Тест для проверки функции применения скидки"""
    data.pay_rate = 0.7
    data.apply_discount()
    assert data.price == 35000


def test_instantiate_from_csv():
    """Тест для класс-метода, проверяет все ли товары загружены и совпадение с конкретным товаром"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[1]
    assert item1.name == "Ноутбук"
    assert item1.price == 1000
    assert item1.quantity == 3


def test_string_to_number():
    """Тест для статического метода получения числа из строки"""
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('10.1') == 10
