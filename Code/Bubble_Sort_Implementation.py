def bubble_sort(numbers):
    numbers = numbers.copy()

    n = len(numbers)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))

    print("Sorted:", bubble_sort(numbers))
    
# python .\Code\Bubble_Sort_Implementation.py