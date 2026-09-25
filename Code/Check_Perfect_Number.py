def is_perfect(number):
    if number <= 1:
        return False

    divisor_sum = 1

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisor_sum += i

            if i != number // i:
                divisor_sum += number // i

    return divisor_sum == number


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    if is_perfect(number):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
        
# python .\Code\Check_Perfect_Number.py