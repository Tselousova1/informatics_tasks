# Задача 2. Параметры помещения
# Программа рассчитывает площадь пола, площадь стен,
# объём помещения и стоимость покраски стен.

# Размеры помещения в метрах
length = 6.0
width = 5.0
height = 2.8

# Стоимость покраски 1 квадратного метра стены
paint_price = 130

# Расчёты
floor_area = length * width
wall_area = 2 * (length + width) * height
room_volume = length * width * height
paint_cost = wall_area * paint_price

# Вывод результатов
print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print(f"Длина: {length:.2f} м")
print(f"Ширина: {width:.2f} м")
print(f"Высота: {height:.2f} м")
print()
print(f"Площадь пола: {floor_area:.2f} м²")
print(f"Площадь стен: {wall_area:.2f} м²")
print(f"Объём помещения: {room_volume:.2f} м³")
print(f"Стоимость покраски стен: {paint_cost:.2f} руб.")
