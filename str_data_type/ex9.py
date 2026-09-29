vowels = 0
consonants = 0

st = input()

for el in st:
    if el in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        vowels += 1
    elif el in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        consonants += 1
print(f'''Количество гласных букв равно {vowels}
Количество согласных букв равно {consonants}''')