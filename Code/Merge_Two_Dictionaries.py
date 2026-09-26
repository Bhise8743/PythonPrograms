def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)

    return result


if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}

    print(merge_dictionaries(dict1, dict2))
    
# python .\Code\Merge_Two_Dictionaries.py