import importlib

module = importlib.import_module("Code.Find_GCD_and_LCM_of_Two_Numbers")


def test_gcd_lcm():
    assert module.gcd_lcm(12, 18) == (6, 36)


def test_equal_numbers():
    assert module.gcd_lcm(10, 10) == (10, 10)


def test_coprime_numbers():
    assert module.gcd_lcm(7, 13) == (1, 91)


def test_zero():
    assert module.gcd_lcm(0, 5) == (5, 0)


def test_negative_numbers():
    assert module.gcd_lcm(-12, 18) == (6, 36)
    
# python -m pytest .\Test_Code\Test_Find_GCD_and_LCM_of_Two_Numbers.py