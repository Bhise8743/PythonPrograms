import importlib

module = importlib.import_module("Code.Check_Positive_Negative_Zero_Num")


def test_positive():
    assert module.check_number(10) == "Positive"


def test_negative():
    assert module.check_number(-10) == "Negative"


def test_zero():
    assert module.check_number(0) == "Zero"


def test_positive_decimal():
    assert module.check_number(2.5) == "Positive"


def test_negative_decimal():
    assert module.check_number(-2.5) == "Negative"
    
# python -m pytest .\Test_Code\Test_Check_Positive_Negative_Zero_Num.py
