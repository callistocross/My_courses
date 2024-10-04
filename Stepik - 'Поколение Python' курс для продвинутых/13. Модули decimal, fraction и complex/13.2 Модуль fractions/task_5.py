'''
На вход программе подается натуральное число n. Напишите программу, 
которая вычисляет и выводит рациональное число, равное значению 
выражения (1/1^2) + (1/2^2) + (1/3^2) + (1/4^2) + ... + (1/n^2).
'''

# put your python code here
from fractions import Fraction as F

n, sum = int(input()), 0
for i in range(1, n + 1):
    sum += F('1'+ '/' + str(i**2))
print(sum)