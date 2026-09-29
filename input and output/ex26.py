num = int(input())
first_digit = num // 100
second_digit = (num % 100) // 10
last_digit = num % 10

print(f'''Сумма цифр = {first_digit + second_digit + last_digit}
Произведение цифр = {first_digit * second_digit * last_digit}''')