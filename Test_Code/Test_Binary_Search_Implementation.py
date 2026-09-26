import importlib

module = importlib.import_module("Code.Binary_Search_Implementation")


def test_target_found():
    assert module.binary_search(
        [1, 2, 3, 4, 5], 3
    ) == 2


def test_first_element():
    assert module.binary_search(
        [1, 2, 3, 4, 5], 1
    ) == 0


def test_last_element():
    assert module.binary_search(
        [1, 2, 3, 4, 5], 5
    ) == 4


def test_target_not_found():
    assert module.binary_search(
        [1, 2, 3, 4, 5], 10
    ) == -1


def test_empty_list():
    assert module.binary_search([], 5) == -1


def test_duplicate_values():
    result = module.binary_search([1, 2, 2, 2, 3], 2)

    assert result in [1, 2, 3]
    
