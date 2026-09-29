lst = [input() for _ in range(3)]
len1, len2, len3 = len(lst[0]), len(lst[1]), len(lst[2])
mx_len = max(len1, len2, len3)
mn_len = min(len1, len2, len3)
for el in lst:
    if len(el) == mn_len:
        print(el)
for el in lst:
    if len(el) == mx_len:
        print(el)


