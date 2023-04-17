# Ввод даты строкой
date_str = input("Введите дату в формате 'ДД МЕСЯЦ': ")

# Разбиение даты на составляющие
date_parts = date_str.split()
day = int(date_parts[0])
month_name = date_parts[1]

# Преобразование названия месяца в номер месяца
months = {
    'января': 1,
    'февраля': 2, 
    'марта': 3, 
    'апреля': 4, 
    'мая': 5, 
    'июня': 6, 
    'июля': 7, 
    'августа': 8, 
    'сентября': 9, 
    'октября': 10, 
    'ноября': 11, 
    'декабря': 12
}
month = months[month_name]

# Проверка корректности введенной даты
days_in_month = {
    1: 31, 
    2: 28, 
    3: 31, 
    4: 30, 
    5: 31, 
    6: 30, 
    7: 31, 
    8: 31, 
    9: 30, 
    10: 31, 
    11: 30, 
    12: 31
}
if month not in months.values() or day > days_in_month[month]:
    print("Такой даты не существует")
else:
    # Определение предыдущей даты
    if day > 1:
        day -= 1
    else: # Новый месяц
        month -= 1
        if month == 0: # Новый год
            month = 12
        day = days_in_month[month]

    # Вывод предыдущей даты
    month_name = list(months.keys())[list(months.values()).index(month)]
    print(f"Предыдущая дата: {day} {month_name}")
