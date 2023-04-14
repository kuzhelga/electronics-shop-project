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