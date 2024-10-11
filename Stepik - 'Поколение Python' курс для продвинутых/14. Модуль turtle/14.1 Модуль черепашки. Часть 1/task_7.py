'''
Напишите программу, которая рисует ромб с углами 60 и 120 градусов.
'''
import turtle

def rhombus(a):
    for num in [120, 60, 120, 60]:
        turtle.forward(a)
        turtle.left(num)          
a = int(input())
rhombus(a)
turtle.mainloop()