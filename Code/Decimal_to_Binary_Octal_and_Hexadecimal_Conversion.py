def convert_number(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    binary = bin(number)[2:]
    octal = oct(number)[2:]
    hexadecimal = hex(number)[2:].upper()

    return binary, octal, hexadecimal


if __name__ == "__main__":
    number = int(input("Enter a decimal number: "))

    binary, octal, hexadecimal = convert_number(number)

    print("Binary:", binary)
    print("Octal:", octal)
    print("Hexadecimal:", hexadecimal)
    
