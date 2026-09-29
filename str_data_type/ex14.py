st = input()
print(st[(len(st) % 2) + (len(st) // 2):] + st[:(len(st) % 2) + (len(st) // 2)])