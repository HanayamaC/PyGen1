a, b = int(input()), int(input())
max_digit = 0
max_total = 0
for i in range(a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
    if total >= max_total:
        if i > max_digit:
            max_total = total
            max_digit = i
print(f'{max_digit} {max_total}')