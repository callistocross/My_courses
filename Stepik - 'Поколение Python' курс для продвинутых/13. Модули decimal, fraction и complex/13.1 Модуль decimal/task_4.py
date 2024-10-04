'''
На вход программе подается Decimal число d. Напишите программу, 
которая вычисляет значение выражения: e^d + ln(d) + lg(d) + sqrt(d).
'''

# put your python code here
from decimal import *

d = Decimal(input())
print(d.exp() + d.ln() + d.log10() + d.sqrt())