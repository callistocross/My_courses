'''
Даны два натуральных числа m и n. Напишите программу, которая 
сокращает дробь m/n и выводит ее.
'''

# put your python code here
from fractions import Fraction
print(Fraction(input() + '/' + input()))