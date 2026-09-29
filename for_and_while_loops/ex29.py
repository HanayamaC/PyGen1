counter = 0

grade = int(input())

while 5 >= grade > 0:
    if grade == 5:
        counter += 1
    grade = int(input())
        
print(counter)