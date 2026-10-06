numbers = [10, 20, 30, 40, 50, 60]

search = int(input("Enter number: "))

low = 0
high = len(numbers) - 1

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == search:
        print("Element found")
        break

    elif search > numbers[mid]:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Element not found")
