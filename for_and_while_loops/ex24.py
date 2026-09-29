n = int(input())

lst = [int(input()) for _ in range(n)]
print(sorted(lst)[-1], sorted(lst)[-2], sep='\n')