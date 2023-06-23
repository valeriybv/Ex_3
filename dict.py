#Дан список произвольной длины.
# Необходимо написать код, который на основе исходного списка составит словарь такого уровня вложенности,
# какова длина исхондого списка.
my_list = ['2018-01-01']
my_list2 = ['2018-01-01', 'dfdsf']
my_list3 = ['a', 'b', 'c', 'd', 'e', 'f']


def check_list(list):
    if len(list) < 2:
        return 0
    else:
        return 1


def dict_constructor(key, value):
    dict = {}
    dict[key] = value
    return dict


def list_to_dict(list):
    if (check_list(list) == 0):
        return ("Список должен содержать более одного элемента!")
    else:
        for i in range(1, len(list)+1):
            if i == 2:
                iter = len(list) - i
                value = list[iter + 1]
                key = list[iter]
                dict = dict_constructor(key, value)
                if (len(list)) == 2:
                    return dict
            if i > 2:
                iter = len(list) - i
                value = dict
                key = list[iter]
                dict = dict_constructor(key, value)
        return dict


result = list_to_dict(my_list3)
print(result)
