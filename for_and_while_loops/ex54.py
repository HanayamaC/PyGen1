n, m = int(input()), int(input())
cnt = 0
for banana in range(1, n):
    for diamond in range(1, n):
        for deer in range(1, n):
            if banana + 3 * diamond + 2 * deer == m:
                print(f'{banana} + 3×{diamond} + 2×{deer} = {m}')
                cnt += 1
if cnt == 0:
    print('При заданных n и m решений не существует.')