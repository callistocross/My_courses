'''
Даны две дроби в формате a/b. Напишите программу, которая 
вычисляет и выводит их сумму, разность, произведение и частное.
'''

# put your python code here
from fractions import Fraction
from operator import add, sub, mul, truediv

num1, num2 = input(), input()
op, ops = '+-*/', [add, sub, mul, truediv]
oprs = dict(zip(op, ops))
[print(f'{num1} {i} {num2} = {oprs[i](Fraction(num1), Fraction(num2))}') for i in op]