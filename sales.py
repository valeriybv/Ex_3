#Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж (пример структуры данных приведен ниже).
# Напишите программу, которая возвращает название канала с максимальным объемом продаж.
stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}


def get_max_sales(data):
    return max(data, key=data.get)


max_sales_channel = get_max_sales(stats)
print("Максимальный объем продаж на рекламном канале:", max_sales_channel)