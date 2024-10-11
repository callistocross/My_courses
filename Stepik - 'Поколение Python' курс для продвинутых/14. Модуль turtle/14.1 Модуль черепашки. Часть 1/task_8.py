'''
Напишите программу, которая рисует снежинку из 10 ромбов.
'''
import turtle
n = 10 # кол-во ромбов
def rhombus(side, n):
    turtle.left(360 / n) 
    a, b = 50, 130
    for num in [a, b]*2:
        turtle.forward(side)
        turtle.left(num)          
side = 80
for _ in range(n):
    rhombus(side, n)
turtle.mainloop()