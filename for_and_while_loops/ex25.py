n = int(input())

x1 = 1
x2 = 0

for _ in range(n):
    x1, x2 = x2, x2 + x1
    print(x2, end=' ')



