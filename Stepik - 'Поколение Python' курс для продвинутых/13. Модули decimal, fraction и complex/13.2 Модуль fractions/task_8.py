'''
На вход программе подается натуральное число n. Напишите программу, 
которая выводит в порядке возрастания все несократимые дроби, заключённые между 
0 и 1, знаменатель которых не превосходит n.
'''
from fractions import Fraction as F
n = int(input())
# s = set()
# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         # if i < j:
#             print(f'{i}/{j} =', F(i, j))
#             s.add(F(i, j))
# # print(*sorted(s), sep = '\n')

print(*sorted({F(i, j) for i in range(1, n + 1) for j in range(i, n + 1) if i < j}), sep = '\n')