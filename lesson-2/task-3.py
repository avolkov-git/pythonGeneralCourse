"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
весна, лето, осень). Напишите решения через list и через dict.
"""

while True:
    try:
        usrInput = int(input('Введите месяц числом: '))
    except ValueError:
        print('Вы должны ввести число')
        continue

    if not (0 < usrInput <= 12):
        print('Число должно быть в диапазоне от 1 до 12')
    else:
        break

# Вариант решения с использованием dict
seasons = {'winter': {12, 1, 2}, 'spring': {3, 4, 5}, 'summer': {6, 7, 8}, 'autumn': {9, 10, 11}}

for season_element in seasons.items():
    season_set = season_element[1]
    if usrInput in season_set:
        print('You season is ' + season_element[0])
        break

# Вариант решения с использованием list
winter_list = ['winter', 12, 1, 2]
spring_list = ['spring', 3, 4, 5]
summer_list = ['summer', 6, 7, 8]
autumn_list = ['autumn', 9, 10, 11]

season_list = [winter_list, spring_list, summer_list, autumn_list]

for season_elements in season_list:
    # if season_elements.index(usrInput, 1, 3):
    if season_elements.count(usrInput):
        print('You season is ' + season_elements[0])
        break
