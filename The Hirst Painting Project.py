
'''
# Damien Hirst paintings

We will be using the package colorgram
'''

import turtle as t
from turtle import Screen
import random
t.colormode(255)


lst_of_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# creating objects
tim = t.Turtle()
tim.hideturtle()

# This is so we do not draw the entire path and set a specific starting location.
tim.penup()
tim.setx(-250)
tim.sety(-150)
tim.speed(0)
y = -150

# This method is used to draw each of the dots horizontally with a random color choice.
def horazontal():
    for i in range(10):
        tim.pendown()
        tim.dot(20, random.choice(lst_of_colors))
        tim.penup()
        tim.forward(50)

# we are making 10 rows of 10 columns.
for j in range(10):
    horazontal()
    y += 50
    tim.setpos(-250, y)

screen = Screen()
# This is so the screen doesn't turn off on its own, but rather by a click.
screen.exitonclick()





