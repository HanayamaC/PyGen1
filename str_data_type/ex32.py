current_day = int(input())
current_weight = float(input())
if current_weight <= 100 - current_day * 0.2:
    print(f'''Все идет по плану
#{current_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {100 - current_day * 0.2} кг''')
else:
    print(f'''Что-то пошло не так
#{current_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {100 - current_day * 0.2} кг''')