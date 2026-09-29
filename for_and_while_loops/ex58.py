# n = int(input())
# while n > 9:
#     n = sum([int(el) for el in str(n)])
# print(n)
cnt = 0
total = 0
mul = 1

n = input()
print(n.count('3'), n.count(n[-1]), sep='\n')

for el in n:
    if int(el) % 2 == 0:
        cnt += 1    
    if int(el) > 5:
        total += int(el)
    if int(el) > 7:
        mul *= int(el)
print(cnt, total, mul, sep='\n')
print(n.count('0') + n.count('5'), sep='\n')
