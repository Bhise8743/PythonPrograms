def fibonacci_series(number):
    if number < 0:
        raise ValueError("Number of terms cannot be negative")

    series = []
    a, b = 0, 1

    for _ in range(number):
        series.append(a)
        a, b = b, a + b

    return series


if __name__ == "__main__":
    number = int(input("Enter number of terms: "))
    print(fibonacci_series(number))
    
# python .\Code\Fibonacci_Series.py  
