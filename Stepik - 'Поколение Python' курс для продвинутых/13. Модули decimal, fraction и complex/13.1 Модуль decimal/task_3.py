'''
Дополните приведенный код, чтобы он вывел сумму наибольшей 
и наименьшей цифры Decimal числа.
'''

from decimal import *
num = Decimal(input())
num_tuple = num.as_tuple()
print(max(num_tuple.digits)) if -1 < num < 1 else print(min(num_tuple.digits) + max(num_tuple.digits))