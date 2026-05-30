# Задача 5. Калькулятор скидки
# Программа рассчитывает стоимость покупки материалов
# с применением прогрессивной системы скидок.

# Исходные данные
price = 60
quantity = 70

# Расчёт общей стоимости без скидки
total_cost = price * quantity

# Определение размера скидки
if total_cost < 1000:
    discount_percent = 0
elif total_cost <= 5000:
    discount_percent = 5
else:
    discount_percent = 10

# Расчёт суммы скидки и итоговой стоимости
discount_amount = total_cost * discount_percent / 100
final_cost = total_cost - discount_amount

# Вывод результата
print("=== КАЛЬКУЛЯТОР СКИДКИ ===")
print(f"Цена товара: {price} руб.")
print(f"Количество: {quantity} шт.")
print(f"Стоимость без скидки: {total_cost:.2f} руб.")
print(f"Размер скидки: {discount_percent}%")
print(f"Сумма скидки: {discount_amount:.2f} руб.")
print(f"Итого к оплате: {final_cost:.2f} руб.")
