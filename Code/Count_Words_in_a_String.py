def count_words(text):
    return len(text.split())


if __name__ == "__main__":
    text = input("Enter a string: ")

    print("Number of words:", count_words(text))
    
# python .\Code\Count_Words_in_a_String.py