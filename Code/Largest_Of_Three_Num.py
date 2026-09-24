def largest_of_three(a, b, c):
    return max(a, b, c)


if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    print("Largest:", largest_of_three(a, b, c))
    
# python .\Code\Largest_Of_3_Num.py 