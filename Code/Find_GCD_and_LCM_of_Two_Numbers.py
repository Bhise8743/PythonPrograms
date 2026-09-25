import math


def gcd_lcm(a, b):
    gcd = math.gcd(a, b)

    if a == 0 or b == 0:
        lcm = 0
    else:
        lcm = abs(a * b) // gcd

    return gcd, lcm


if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    gcd, lcm = gcd_lcm(a, b)

    print("GCD:", gcd)
    print("LCM:", lcm)
    
# python .\Code\Find_GCD_and_LCM_of_Two_Numbers.py