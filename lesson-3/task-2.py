# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def print_user_information(user_name='', user_surname='', user_birth_year='', user_city='', user_email='',
                           user_tel_number=''):
    print(
        f'Пользователь: {user_name} {user_surname}, {user_birth_year} года рождения. Проживает в городе {user_city}. '
        f'Контакты: Телефон({user_tel_number}), email({user_email})')


name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
birth_year = input('Введите год Вашего рождения: ')
city = input('В каком городе Вы проживаете: ')
email = input('Введите Ваш адрес электронной почты: ')
tel_number = input('Контактный телефон: ')

print_user_information(user_name=name, user_surname=surname, user_birth_year=birth_year,
                       user_city=city, user_email=email, user_tel_number=tel_number)
