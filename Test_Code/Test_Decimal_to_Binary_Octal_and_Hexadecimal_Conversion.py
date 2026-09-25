import importlib
import pytest

module = importlib.import_module("Code.Decimal_to_Binary_Octal_and_Hexadecimal_Conversion")


def test_zero():
    assert module.convert_number(0) == ("0", "0", "0")


def test_number_10():
    assert module.convert_number(10) == ("1010", "12", "A")


def test_number_15():
    assert module.convert_number(15) == ("1111", "17", "F")


def test_number_255():
    assert module.convert_number(255) == ("11111111", "377", "FF")


def test_negative_number():
    with pytest.raises(ValueError):
        module.convert_number(-10)
        
