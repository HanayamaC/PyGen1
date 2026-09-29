num = int(input())
a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10
if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')