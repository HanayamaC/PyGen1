st = input()
counter = 0
for el in st:
    if el in '0123456789':
        counter += 1
print(counter)