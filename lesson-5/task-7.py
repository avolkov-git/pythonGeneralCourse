# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json


def split_corp_data(date):
    _corp_name, _ownership_form, _income, _costs = date.split()
    return _corp_name, _ownership_form, int(_income), int(_costs)


result_list = []

with open('task-7.txt', 'r', encoding='utf-8') as txt_file:
    items_count = len(txt_file.readlines())
    txt_file.seek(0)

    corp_with_profit = 0
    corp_dict = {}
    average_profit = {'average_profit': 0}

    for index in range(items_count):
        # Получаем данные
        corp_data = txt_file.readline().rstrip('\n')
        corp_name, ownership_form, income, costs = split_corp_data(corp_data)

        # Добавляем в список фирм (если прибыль отрицательная, инвертируем значение)
        corp_dict[corp_name] = (income - costs) if (income - costs) > 0 else (income - costs) * -1

        # Добавляем прибыль в показатель средней прибыли (если убыток, то не добавляем)
        average_profit['average_profit'] += (income - costs) if (income - costs) > 0 else 0

        if (income - costs) > 0:
            corp_with_profit += 1

    # Считаем среднюю прибыль
    if average_profit['average_profit'] > 0:
        average_profit['average_profit'] /= corp_with_profit

    result_list = [corp_dict, average_profit]

with open('task-7.json', 'w', encoding='utf-8') as json_file:
    json.dump(result_list, json_file)
