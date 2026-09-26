def fibonacci_recursive(number):
    if number < 0:
        raise ValueError("Number cannot be negative")

    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


def fibonacci_series(number):
    if number < 0:
        raise ValueError("Number of terms cannot be negative")

    return [fibonacci_recursive(i) for i in range(number)]


if __name__ == "__main__":
    number = int(input("Enter number of terms: "))

    print(fibonacci_series(number))
    
