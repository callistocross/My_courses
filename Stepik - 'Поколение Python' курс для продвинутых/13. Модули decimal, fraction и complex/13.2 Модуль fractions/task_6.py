'''
На вход программе подается натуральное число n. Напишите программу, 
которая вычисляет и выводит рациональное число, равное значению 
выражения (1/1!) + (1/2!) + (1/3!) + (1/4!) + ... + (1/n!).
'''

from math import factorial as fact
from fractions import Fraction as F
n = int(input())
print(sum([F(1, fact(i)) for i in range(1, n + 1)]))

 