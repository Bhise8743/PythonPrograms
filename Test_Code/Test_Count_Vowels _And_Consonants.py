import importlib

module = importlib.import_module("Code.Count_Vowels _And_Consonants")


def test_simple_word():
    assert module.count_vowels_consonants("hello") == (2, 3)


def test_all_vowels():
    assert module.count_vowels_consonants("aeiou") == (5, 0)


def test_all_consonants():
    assert module.count_vowels_consonants("bcdfg") == (0, 5)


def test_with_spaces():
    assert module.count_vowels_consonants("hello world") == (3, 7)


def test_empty_string():
    assert module.count_vowels_consonants("") == (0, 0)


def test_uppercase():
    assert module.count_vowels_consonants("HELLO") == (2, 3)
    
# python -m pytest '.\Test_Code\Test_Count_Vowels _And_Consonants.py'
