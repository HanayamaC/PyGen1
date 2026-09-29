n = int(input())
for h in range(24):
    for m in range(60):
        if h**n == m:
            print(f'{h:02}:{m:02}')