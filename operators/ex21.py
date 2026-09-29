num1 = int(input())
num2 = int(input())
op = input()

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    if num2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(num1 / num2)
else:
    print('Неверная операция')