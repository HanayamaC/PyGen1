color1, color2 = input(), input()
set1 = ['красный', 'синий']
set2 = ['красный', 'желтый']
set3 = ['синий', 'желтый']

if color1 in ['красный', 'синий', 'желтый'] and color1 == color2:
    print(color1)
elif [color1, color2] == set1 or [color1, color2] == set1[::-1]:
    print('фиолетовый')
elif [color1, color2] == set2 or [color1, color2] == set2[::-1]:
    print('оранжевый')
elif [color1, color2] == set3 or [color1, color2] == set3[::-1]:
    print('зеленый')
else:
    print('ошибка цвета')