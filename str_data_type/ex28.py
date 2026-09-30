nickname = input()
if (15 >= len(nickname) >= 5
    and nickname[0] == '@'
    and nickname[1:].isalnum()
    and nickname == nickname.lower()):
        print('Correct')
else:
    print('Incorrect')