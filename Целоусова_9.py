# Задача 9. Очистка адресов
# Программа приводит адреса объектов к стандартному формату.

# Исходный список адресов
addresses = [
    " г. Москва, ул. Ленина, д. 10 ",
    "г.Казань,ул.Баумана,д.15",
    " г. Санкт-Петербург, ул. Невский, д. 100 "
]

# Вывод заголовка
print("=== СРАВНЕНИЕ ===")

# Обработка адресов
for i, address in enumerate(addresses, 1):
    cleaned = address.strip()
    cleaned = cleaned.replace("г.", "г. ")
    cleaned = cleaned.replace("ул.", "ул. ")
    cleaned = cleaned.replace("д.", "д. ")
    cleaned = cleaned.replace(",", ", ")
    cleaned = " ".join(cleaned.split())

    print(f"#{i}")
    print(f"ДО: '{address}'")
    print(f"ПОСЛЕ: '{cleaned}'")
