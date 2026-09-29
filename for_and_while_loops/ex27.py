counter = 0
word = input()
while word not in ['стоп', 'хватит', 'достаточно']:
    counter += 1
    word = input()
print(counter)