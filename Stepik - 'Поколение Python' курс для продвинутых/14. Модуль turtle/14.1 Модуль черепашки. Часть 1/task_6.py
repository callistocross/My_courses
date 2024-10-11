'''
Напишите программу, которая рисует соты.
'''
import turtle

def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)
           
side = int(input())
for _ in range(6):
    hexagon(side)
    turtle.right(120)
    turtle.forward(side)
    turtle.left(60)
turtle.mainloop()