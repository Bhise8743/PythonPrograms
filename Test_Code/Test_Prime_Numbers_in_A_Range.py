import importlib

module = importlib.import_module("Code.Prime_Numbers_in_A_Range")


def test_range_1_to_10():
    assert module.primes_in_range(1, 10) == [2, 3, 5, 7]


def test_range_10_to_20():
    assert module.primes_in_range(10, 20) == [11, 13, 17, 19]


def test_range_with_no_primes():
    assert module.primes_in_range(8, 10) == []


def test_single_prime():
    assert module.primes_in_range(7, 7) == [7]


def test_single_non_prime():
    assert module.primes_in_range(8, 8) == []
    
    
# python -m pytest .\Test_Code\Test_Prime_Numbers_in_A_Range.py
