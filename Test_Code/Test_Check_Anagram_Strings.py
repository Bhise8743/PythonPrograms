import importlib

module = importlib.import_module("Code.Check_Anagram_Strings")


def test_anagrams():
    assert module.are_anagrams("listen", "silent") is True


def test_anagrams_with_spaces():
    assert module.are_anagrams(
        "conversation",
        "voices rant on"
    ) is True


def test_not_anagrams():
    assert module.are_anagrams("hello", "world") is False


def test_case_insensitive():
    assert module.are_anagrams("Listen", "Silent") is True


def test_empty_strings():
    assert module.are_anagrams("", "") is True
    
# python -m pytest .\Test_Code\Test_Check_Anagram_Strings.py