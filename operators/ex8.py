age = int(input())
if age <= 13:
    print('детство')
elif 24 >= age > 13:
    print('молодость')
elif 59 >= age > 24:
    print('зрелость')
else:
    print('старость')