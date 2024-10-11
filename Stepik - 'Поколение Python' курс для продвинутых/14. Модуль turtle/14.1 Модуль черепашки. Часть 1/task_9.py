'''
Напишите программу, которая рисует лучи звезды, показанной на рисунке.
'''
import turtle
side = int(input())
angle = 30
for _ in range(360//angle):
    turtle.forward(side)
    turtle.backward(side)
    turtle.left(angle)
turtle.mainloop()