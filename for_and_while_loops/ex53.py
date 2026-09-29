n = int(input())

total = 0

for i in range(1, n + 1):
    mul = 1
    for j in range(1, i + 1):
        mul *= j
    total += mul
print(total)