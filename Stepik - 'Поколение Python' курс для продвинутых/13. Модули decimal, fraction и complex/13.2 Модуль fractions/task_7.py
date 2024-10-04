'''
На вход программе подается натуральное число n. Напишите программу, 
которая находит наибольшую правильную несократимую дробь 
с суммой числителя и знаменателя равной n.
'''
from fractions import Fraction as F
n = int(input())
# s = set()
# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         if (i < j) and (F(i, j).numerator + F(i, j).denominator == n):
#             print(f'{i}/{j} =', F(i, j))
#             s.add(F(i, j))
# print(*sorted(s, reverse=True)[:1], sep = '\n')

print(*sorted({F(i, j) for i in range(1, n + 1) for j in range(i, n + 1) if (i < j) and (F(i, j).numerator + F(i, j).denominator == n)}, reverse=True)[:1], sep = '\n')
