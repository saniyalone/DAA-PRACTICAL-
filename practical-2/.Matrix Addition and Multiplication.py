r, c = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(r)]
B = [list(map(int, input().split())) for _ in range(r)]

print("Addition")

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    print(row)

print("Multiplication")

for i in range(r):
    row = []
    for j in range(c):
        s = 0
        for k in range(c):
            s += A[i][k] * B[k][j]
        row.append(s)
    print(row)
