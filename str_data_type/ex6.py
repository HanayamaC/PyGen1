st = input()
for el in st:
    if el in '0123456789':
        print('Цифра')
        break
else:
    print('Цифр нет')