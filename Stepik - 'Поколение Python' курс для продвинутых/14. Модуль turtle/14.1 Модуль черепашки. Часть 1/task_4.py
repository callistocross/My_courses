'''
Напишите программу, которая рисует изображенную фигуру из восьми квадратов.
'''
import turtle

def square(side):
  turtle.left(45)
  for _ in range(4):
    turtle.forward(side)
    turtle.left(90)
  
side = int(input())
for i in range(8):
  square(side)
turtle.mainloop()