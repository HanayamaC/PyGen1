# analyze_sales.py

# 1. Чтение данных из файла

# 2. Преобразование строк в числа

# 3. Расчёт статистики

# 4. Вывод в консоль

# 5. Запись в файл report.txt

with open('sales.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
sales = []

for line in lines:
    clean_line = line.strip()
    if clean_line:
        number = int(clean_line)
        sales.append(number)
        
total = sum(sales)
mx = max(sales)
mn = min(sales)
count = len(sales)
average = total / count

print("📊 Отчёт по продажам")
print(f"Всего дней: {count}")
print(f"Общая выручка: {total} руб.")
print(f"Средняя выручка: {average:.2f} руб.")   # два знака после запятой
print(f"Максимум: {mx} руб.")
print(f"Минимум: {mn} руб.")