#Дана переменная, в которой хранится список поисковых запросов пользователя
# (пример структуры данных приведен ниже, но запросы потенциально могут быть любые).
# Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.

import pandas as pd

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'fdjkfl jkjklj сериалы про спорт porn     d d '
]


def get_words_distribution(queries):
    count = list()
    for item in queries:
        count.append(len(item.split()))
    return (pd.Series(count).value_counts(normalize=True).sort_index())


def print_distribution(distr):
    for key, value in distr.items():
        print ("Поисковых запросов, содержащих", key, "слов(а):", value*100,"%")


words_count = get_words_distribution(queries)
print_distribution(words_count)