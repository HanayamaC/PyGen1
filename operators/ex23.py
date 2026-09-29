pocket = int(input())
if pocket == 0:
    print('зеленый')
elif 10 >= pocket >= 1:
    if pocket % 2 == 1:
        print('красный')
    else:
        print('черный')
elif 18 >= pocket >= 11:
    if pocket % 2 == 1:
        print('черный')
    else:
        print('красный')
elif 28 >= pocket >= 19:
    if pocket % 2 == 1:
        print('красный')
    else:
        print('черный')
elif 36 >= pocket >= 29:
    if pocket % 2 == 1:
        print('черный')
    else:
        print('красный')
else:
    print('ошибка ввода')