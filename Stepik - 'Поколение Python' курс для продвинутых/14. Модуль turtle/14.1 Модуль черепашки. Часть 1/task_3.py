'''
Напишите программу, которая рисует изображенную фигуру, состоящую из трех квадратов.
'''
import turtle

def square(side):
  for num in [30, 45, 60]:
    turtle.setheading(num)
    for _ in range(4):
      turtle.forward(side)
      turtle.left(90)
  
side = int(input())
square(side)
turtle.mainloop()