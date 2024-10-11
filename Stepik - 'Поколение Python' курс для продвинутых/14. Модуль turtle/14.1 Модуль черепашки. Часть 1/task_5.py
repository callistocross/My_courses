'''
Напишите программу, которая рисует правильный шестиугольник.
'''

import turtle

def hexagon(side):
  for _ in range(6):
    turtle.left(60)
    turtle.forward(side)
  
side = int(input())
hexagon(side)
turtle.mainloop()