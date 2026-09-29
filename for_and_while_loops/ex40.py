flag = False

n = [int(el) for el in input()]
for i in range(len(n) - 1):
    if n[i] < n[i + 1]:
        flag = True
        break
if flag:
    print('NO')
else:
    print('YES')