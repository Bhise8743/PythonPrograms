import importlib

module = importlib.import_module("Code.Convert_a_Sentence_to_Title_Case")


def test_title_case():
    assert module.title_case(
        "hello world"
    ) == "Hello World"


def test_lowercase_sentence():
    assert module.title_case(
        "python is easy to learn"
    ) == "Python Is Easy To Learn"


def test_uppercase_sentence():
    assert module.title_case(
        "HELLO WORLD"
    ) == "Hello World"


def test_empty_string():
    assert module.title_case("") == ""


def test_single_word():
    assert module.title_case("python") == "Python"
    
# python -m pytest .\Test_Code\Test_Convert_a_Sentence_to_Title_Case.py