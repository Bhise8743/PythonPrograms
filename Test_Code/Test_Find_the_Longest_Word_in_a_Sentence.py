import importlib

module = importlib.import_module("Code.Find_the_Longest_Word_in_a_Sentence")


def test_longest_word():
    assert module.longest_word(
        "Python programming is interesting"
    ) == "programming"


def test_single_word():
    assert module.longest_word("Python") == "Python"


def test_empty_sentence():
    assert module.longest_word("") == ""


def test_same_length_words():
    assert module.longest_word(
        "cat dog"
    ) == "cat"


def test_extra_spaces():
    assert module.longest_word(
        "I love programming"
    ) == "programming"
    
#  python -m pytest .\Test_Code\Test_Find_the_Longest_Word_in_a_Sentence.py