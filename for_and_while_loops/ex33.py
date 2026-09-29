h1, m1, h2, m2 = int(input()) * 60, int(input()), int(input()) * 60, int(input())
for i in range(h1 + m1, h2 + m2 + 1):
    print(print("%02d:%02d" % (i // 60, i % 60)))
    