n = int(input())
for i in range(1, n + 1):
    print(i, end='')
    for j in range(i, i + 1):
        if i % j == 0:
            print('+', end='')
    print()