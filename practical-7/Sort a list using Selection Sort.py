numbers = [50, 20, 40, 10, 30]

for i in range(len(numbers)):

    minimum = i

    for j in range(i + 1, len(numbers)):

        if numbers[j] < numbers[minimum]:
            minimum = j

    numbers[i], numbers[minimum] = \
        numbers[minimum], numbers[i]

print(numbers)
