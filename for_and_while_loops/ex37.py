n = [int(el) for el in input()]

total = 1

print(sum(n), len(n), sep='\n')

for el in n:
    total *= el
print(total)

print(sum(n) / len(n), n[0], n[0] + n[-1], sep='\n')