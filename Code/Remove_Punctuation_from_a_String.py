import string


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


if __name__ == "__main__":
    text = input("Enter a string: ")

    print(remove_punctuation(text))
    
# python .\Code\Remove_Punctuation_from_a_String.py