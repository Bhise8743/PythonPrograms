# Reverse a String Without [::-1] 
def reverse_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Reversed:", reverse_string(text))
    
# python .\Code\Reverse_A_String.py