'''
Напишите программу, которая рисует узор, показанный на рисунке.
'''
import turtle
turtle.pensize(2)
for i in range(10, 255, 5):
    turtle.left(90)
    turtle.forward(i)

turtle.mainloop()