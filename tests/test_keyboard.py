from src.keyboard import KeyBoard
import pytest


@pytest.fixture
def new_keyboard():
    return KeyBoard("Redwings", 7500, 6)


def test_change_lang(new_keyboard):

    assert str(new_keyboard) == "Redwings"


def test_language(new_keyboard):

    assert str(new_keyboard.language) == "EN"

    new_keyboard.change_lang()
    assert str(new_keyboard.language) == "RU"
