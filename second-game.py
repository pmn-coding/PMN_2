from turtle import *
from random import *

# --------------------------------------WINDOW--------------------------------------

window = Screen()
window.title("Pong")
window.bgcolor("lightgreen")
window.setup(width=800, height=600)
window.tracer()

# --------------------------------------SCOREBOARD--------------------------------------

# --------------------------------------Paddle 1--------------------------------------

paddle_1 = Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("black")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-385, 0)

# --------------------------------------Paddle 2--------------------------------------

paddle_2 = Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("black")
paddle_2.shapesize(stretch_wid=5, stretch_len=1, outline=1)
paddle_2.penup()
paddle_2.goto(+380, 0)

# --------------------------------------Ball 1--------------------------------------

ball = Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)

ball.dx = 2
ball.dy = -2

# --------------------------------------Def's--------------------------------------

def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y) 

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y) 

# --------------------------------------BINDS--------------------------------------

window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")


# --------------------------------------Main --------------------------------------

while True:
    window.update()
    
    # Move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Prove Limes

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -282:
        ball.sety(-282)
        ball.dy *= -1

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -385:
        ball.goto(0, 0)
        ball.dx *= -1

    # TOUCH THE SHIT

    if ball.xcor() < -365 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1 
        bb = randint(1,4)
        if bb == 1:
            ball.color("Indian Red")
            paddle_2.color("Indian Red")
            window.bgcolor("lightgreen")
        elif bb == 2:
            ball.color("lightblue")
            paddle_2.color("lightblue")
            window.bgcolor("green")
        elif bb == 3:
            ball.color("purple")
            paddle_2.color("purple")
            window.bgcolor("mediumseagreen")
        else:
            ball.color("black")
            paddle_2.color("black")
            window.bgcolor("darkgreen")
        

    elif ball.xcor() > 360 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        bb = randint(1,4)
        if bb == 1:
            ball.color("Indian Red")
            paddle_1.color("Indian Red")
            window.bgcolor("lightgreen")
        elif bb == 2:
            ball.color("lightblue")
            paddle_1.color("lightblue")
            window.bgcolor("green")
        elif bb == 3:
            ball.color("purple")
            paddle_1.color("purple")
            window.bgcolor("mediumseagreen")
        else:
            ball.color("black")
            paddle_1.color("black")
            window.bgcolor("darkgreen")



