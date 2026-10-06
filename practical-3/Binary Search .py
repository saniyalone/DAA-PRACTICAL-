a = sorted(list(map(int, input().split())))
key = int(input())

l = 0
r = len(a) - 1

while l <= r:
    m = (l + r) // 2

    if a[m] == key:
        print("Found")
        break
    elif key < a[m]:
        r = m - 1
    else:
        l = m + 1
else:
    print("Not Found")
