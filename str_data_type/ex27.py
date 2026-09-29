n = int(input())
for i in range(1, n + 1):
    comment = input()
    if comment.isspace() or comment == '':
        print(f'{i}: COMMENT SHOULD BE DELETED')
    else:
        print(f'{i}: {comment}')