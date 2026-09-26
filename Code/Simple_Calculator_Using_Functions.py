def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


def calculate(a, b, operator):
    if operator == "+":
        return add(a, b)

    elif operator == "-":
        return subtract(a, b)

    elif operator == "*":
        return multiply(a, b)

    elif operator == "/":
        return divide(a, b)

    else:
        raise ValueError("Invalid operator")


if __name__ == "__main__":
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    print("Result:", calculate(a, b, operator))
    
# python .\Code\Simple_Calculator_Using_Functions.py