num = [int(el) for el in input()]
i = 0
for el in num:
    if el % 2 == 0:
        i += 1
        print(f'{i}-я четная цифра равна {el}')
if i == 0:
    print('Четных цифр в числе нет')
