n = int(input())
mx = 0
mn = 9
while n != 0:
    last_digit = n % 10
    if last_digit >= mx:
        mx = last_digit
    if last_digit <= mn:
        mn = last_digit
    n //= 10
print(f'''Максимальная цифра равна {mx}
Минимальная цифра равна {mn}''')