len_a, len_b, len_c = len(input()), len(input()), len(input())
print('YES') if (2 * len_b - len_c - len_a) * (2 * len_c - len_b - len_a) * (2 * len_a - len_b - len_c) == 0 else print('NO')