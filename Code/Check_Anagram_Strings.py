# An anagram string is a string formed by rearranging the 
# characters of another string without changing or 
# adding any characters.

def are_anagrams(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    return sorted(string1) == sorted(string2)


if __name__ == "__main__":
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")

    if are_anagrams(string1, string2):
        print("Anagrams")
    else:
        print("Not Anagrams")
        
# python -m pytest .\Test_Code\Test_Check_Anagram_Strings.py