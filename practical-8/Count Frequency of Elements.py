numbers = [10, 20, 10, 30, 20, 10]

frequency = {}

for number in numbers:

    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)

OUTPUT-:
{10: 3, 20: 2, 30: 1}
