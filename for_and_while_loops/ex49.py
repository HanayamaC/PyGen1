for bull in range(1, 11):
    for korova in range(1, 21):
        for tel in range(1, 201):
            if 10 * bull + 5 * korova + 0.5 * tel == 100:
                print(f'Бык = {bull}, корова = {korova}, теленок = {tel}')