from turtle import Turtle
from random import randint

jay = Turtle()
kai = Turtle()
zane = Turtle()
cole = Turtle()

win = Turtle()
win.hideturtle()

jay.color('blue')
kai.color('red')
zane.color('pink')
cole.color('black')

jay.shape('turtle')
kai.shape('turtle')
zane.shape('turtle')
cole.shape('turtle')

jay.penup()
jay.goto(-160,100)
jay.pendown()
kai.penup()
kai.goto(-160,70)
kai.pendown()
zane.penup()
zane.goto(-160,40)
zane.pendown()
cole.penup()
cole.goto(-160,10)
cole.pendown()

for movement in range(100):
    jay.forward(randint(1,5))
    kai.forward(randint(1,5))
    zane.forward(randint(1,5))
    cole.forward(randint(1,5))

winner = max(jay.xcor(), kai.xcor(), zane.xcor(), cole.xcor())
for i in [jay, kai, cole, zane]:
    if i.xcor() == winner:
        win.penup()
        win.goto(i.xcor()+10,i.ycor())
        win.pendown()
        win.write("YEAH!", align="left")

input("Press Enter to close")
