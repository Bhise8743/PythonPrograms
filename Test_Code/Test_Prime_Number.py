import importlib

module = importlib.import_module("Code.Prime_Number")


def test_prime_number():
    assert module.is_prime(7) is True


def test_another_prime():
    assert module.is_prime(13) is True


def test_non_prime():
    assert module.is_prime(10) is False


def test_one():
    assert module.is_prime(1) is False


def test_zero():
    assert module.is_prime(0) is False


def test_negative():
    assert module.is_prime(-7) is False


def test_two():
    assert module.is_prime(2) is True
    
# python -m pytest Test_Code\Test_Prime_Number.py
