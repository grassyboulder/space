from turtle import Turtle, Screen
from random import randint
wn = Screen()
wn.bgcolor('black')
border=Turtle()
border.penup()
border.setpos(-302,-302)
border.pencolor('yellow')
border.pendown()
for side in range(4):
    border.forward(604)
    border.left(90) 
spaceship = Turtle()
spaceship.color('aqua')
spaceship.pendown()
spaceship.pencolor('blue')
speed = 2

def travel():
    spaceship.forward(speed)
    if spaceship.xcor()>300:
        spaceship.seth(randint(120,240))
    if spaceship.ycor()>300:
        spaceship.seth(randint(210,330))
    if spaceship.xcor()<-300:
        spaceship.seth(randint(-60,60))
    if spaceship.ycor()<-300:
        spaceship.seth(randint(30,150))
    wn.ontimer(travel, 10)
    
wn.onkeypress(lambda: spaceship.left(5), 'Left')
wn.onkeypress(lambda: spaceship.right(5), 'Right')
wn.onkeypress(lambda: wn.bye(), "Escape")


wn.listen()

travel()

wn.mainloop()
    