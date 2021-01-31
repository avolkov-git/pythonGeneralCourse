
from sys import argv
from mylib import payroll_calculation

script, name, hours, rate = argv

result = payroll_calculation(hours, rate)
print(f'Employee {name} earned {result}')