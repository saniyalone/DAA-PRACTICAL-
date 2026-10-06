def show(a, i, j):
    if i == len(a):
        return

    print(a[i][j], end=" ")

    if j == len(a[0]) - 1:
        print()
        show(a, i + 1, 0)
    else:
        show(a, i, j + 1)


r, c = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(r)]

show(a, 0, 0)
