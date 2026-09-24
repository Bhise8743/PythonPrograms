import importlib

module = importlib.import_module("Code.Count_Frequency_of_Characters")


def test_simple_string():
    assert module.character_frequency("hello") == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1
    }


def test_repeated_character():
    assert module.character_frequency("aaa") == {"a": 3}


def test_empty_string():
    assert module.character_frequency("") == {}


def test_string_with_spaces():
    assert module.character_frequency("a b") == {
        "a": 1,
        " ": 1,
        "b": 1
    }


def test_case_sensitive():
    assert module.character_frequency("Aa") == {
        "A": 1,
        "a": 1
    }
    
# python -m pytest .\Test_Code\Test_Count_Frequency_of_Characters.py 
