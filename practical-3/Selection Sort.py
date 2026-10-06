a = list(map(int, input().split()))

for i in range(len(a)):
    m = i

    for j in range(i + 1, len(a)):
        if a[j] < a[m]:
            m = j

    a[i], a[m] = a[m], a[i]

print(a)

