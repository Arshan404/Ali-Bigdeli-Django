#روش اول فراخوانی ماژول
import test_modules.calculator

print(test_modules.calculator.sum_number(2, 3))

#روش دوم فراخوانی ماژول

from test_modules.calculator import sum_number

print(sum_number(3,6))

