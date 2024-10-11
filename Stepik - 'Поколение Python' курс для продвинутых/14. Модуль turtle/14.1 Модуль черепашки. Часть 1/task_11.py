'''
Напишите программу, которая рисует квадраты, чтобы создать узор, показанный на рисунке.
'''
import turtle
turtle.pensize(2)
side = 20

def square(side):
  for _ in range(4):
      turtle.left(90)
      turtle.forward(side)
    
for _ in range(30):
    square(side)
    side += 10
turtle.mainloop()