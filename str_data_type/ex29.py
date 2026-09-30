num = input()
flag = False
if 10 >= len(num) >= 9 and num[6] == '_':
    digits = num[1:4] + num[7:]
    letters = num[0] + num[4:6]
    if digits.isdigit() and 6 >= len(digits) >= 5:
        if letters.isalpha:
            for el in letters:
                if el in 'АВЕКМНОРСТУХ':
                    continue
                else:
                    flag = True
                    break
    else:
        flag = True
else:
    flag = True
if flag:
    print('NO')
else:
    print('YES')