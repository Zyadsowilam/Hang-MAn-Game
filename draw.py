#function that draws the hangman
import turtle
from turtle import *
turtle.hideturtle()
color("red")
def Draw(chances):
    #draw y axis
    if chances == 0:
        chances = chances + 1
        left(90)
        forward(200)
        # draw x axis
    elif chances == 1:
        chances = chances + 1
        right(90)
        forward(100)
        # draw rope
    elif chances == 2:
        chances = chances + 1
        right(90)
        forward(40)
        # draw head
    elif chances == 3:
        chances = chances + 1
        color("white")
        right(90)
        color("red")
        turtle.circle(14)
        # draw neck
    elif chances == 4:
        chances = chances + 1
        color("white")
        left(90)
        forward(28)
        color("red")
        forward(20)
        # draw hand
    elif chances == 5:
        chances = chances + 1
        right(90)
        forward(20)
        # draw 2nd hand
    elif chances == 6:
        chances = chances + 1
        turtle.penup()
        left(180)
        forward(20)
        turtle.pendown()
        left(90)
        right(90)
        forward(20)
        # draw hips
    elif chances == 7:
        chances = chances + 1
        turtle.penup()
        right(180)
        forward(20)
        turtle.pendown()
        left(90)
        forward(30)
        # draw leg
    elif chances == 8:
        chances = chances + 1
        left(45)
        forward(20)
    elif chances == 9:
        chances = chances + 1
        turtle.penup()
        left(180)
        forward(20)
        turtle.pendown()
        left(45)
        left(45)
        forward(20)
        turtle.penup()
        forward(200)
        right(90)
        turtle.pendown()
        color("black")
        style = ('Arial', 30, 'bold')
        turtle.write('Game Over', font=style, align='center')

