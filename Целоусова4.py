# Задача 4. Рабочий график
# Программа определяет день недели по его номеру
# и выводит режим работы.

# Номер дня недели
day_number = 2

# Определение дня и режима работы
if day_number == 1:
    day_name = "Понедельник"
    day_type = "Рабочий день"
    work_mode = "9:00 - начало смены"
elif day_number == 2:
    day_name = "Вторник"
    day_type = "Рабочий день"
    work_mode = "9:00 - начало смены"
elif day_number == 3:
    day_name = "Среда"
    day_type = "Рабочий день"
    work_mode = "9:00 - начало смены"
elif day_number == 4:
    day_name = "Четверг"
    day_type = "Рабочий день"
    work_mode = "9:00 - начало смены"
elif day_number == 5:
    day_name = "Пятница"
    day_type = "Рабочий день"
    work_mode = "9:00 - начало смены"
elif day_number == 6:
    day_name = "Суббота"
    day_type = "Выходной"
    work_mode = "Отдых"
elif day_number == 7:
    day_name = "Воскресенье"
    day_type = "Выходной"
    work_mode = "Отдых"
else:
    day_name = "Некорректный номер дня"
    day_type = "-"
    work_mode = "-"

# Вывод результата
print("=== РАБОЧИЙ ГРАФИК ===")
print(f"Номер дня: {day_number}")
print(f"День недели: {day_name}")
print(f"Тип дня: {day_type}")
print(f"Режим: {work_mode}")
