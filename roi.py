# Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам.
# Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: ((revenue / cost) - 1) * 100
results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}


def calculate_roi(data):
    revenue = data['revenue']
    cost = data['cost']
    roi = round(((revenue / cost) - 1) * 100, 2)
    return roi


def add_roi(data):
    for key, value in data.items():
        roi = calculate_roi(value)
        value['roi'] = roi
    return data


data = add_roi(results)
print(data)
