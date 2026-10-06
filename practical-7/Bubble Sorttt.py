numbers = [50, 20, 40, 10, 30]

for i in range(len(numbers)):

    for j in range(len(numbers) - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)

