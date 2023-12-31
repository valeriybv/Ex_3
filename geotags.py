#Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя (пример структуры данных приведен ниже).
# Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех пользователей.

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def get_unique_geotags(ids):
    geotags = list()
    for item in ids.values():
        geotags = geotags + item
    return set(geotags)


unique_geotags = get_unique_geotags(ids)
print(unique_geotags)
