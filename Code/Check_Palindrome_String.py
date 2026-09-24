def is_palindrome_string(text):
    text = text.lower()

    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    text = input("Enter a string: ")

    if is_palindrome_string(text):
        print("Palindrome")
    else:
        print("Not Palindrome")
        
#  python .\Code\Check_Palindrome_String.py