'''
Напишите программу, которая рисует правильную пятиконечную звезду.
'''
import turtle
turtle.pensize(5)
side = int(input())
for _ in range(5):
    turtle.forward(side)
    turtle.right(144)

turtle.mainloop()