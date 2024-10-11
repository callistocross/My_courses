'''
Напишите программу, которая рисует прямоугольник.
'''
import turtle

def rectangle(width, height):
  for _ in range(4):
    turtle.forward(width)
    turtle.left(90)
    width, height = height, width

width, height = int(input()), int(input())
rectangle(width, height)
turtle.mainloop()