def factorial_recursive(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if number == 0 or number == 1:
        return 1

    return number * factorial_recursive(number - 1)


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    print("Factorial:", factorial_recursive(number))
    
#  python .\Code\Factorial_Using_Recursion.py