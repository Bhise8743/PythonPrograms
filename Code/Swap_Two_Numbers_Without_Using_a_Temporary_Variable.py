def swap_numbers(a, b):
    a, b = b, a
    return a, b


if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    a, b = swap_numbers(a, b)

    print("After swapping:")
    print("a =", a)
    print("b =", b)
    
#  python .\Code\Swap_Two_Numbers_Without_Using_a_Temporary_Variable.py         