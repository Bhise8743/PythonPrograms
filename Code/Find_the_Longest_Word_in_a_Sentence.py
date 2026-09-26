def longest_word(sentence):
    words = sentence.split()

    if not words:
        return ""

    return max(words, key=len)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    print("Longest word:", longest_word(sentence))
    
# python .\Code\Find_the_Longest_Word_in_a_Sentence.py