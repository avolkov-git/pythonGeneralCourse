
from random import randint
from mylib import max_numbers_list

number_list = [randint(0, 100) for index in range(10)]
print(number_list)

max_numbers_generator = max_numbers_list(number_list)

result_list = []
for max_number in max_numbers_generator:
    result_list.append(max_number)

print(result_list)
