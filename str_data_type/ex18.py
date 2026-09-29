st = input()
counter = 0
for el in st:
    if el in 'abcdefghijklmnopqrstuvwxyz':
        counter += 1
print(counter)