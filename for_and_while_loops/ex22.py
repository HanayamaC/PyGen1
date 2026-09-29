counter = 0
for _ in range(10):
    num = int(input())
    if num % 2 == 0:
        counter += 1
print('YES') if counter == 10 else print('NO')