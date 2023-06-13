from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forward():
    tim.setheading(0)

    
def move():
    tim.forward(50)


def move_backward():
    tim.setheading(0)
    tim.setheading(180)


def move_clockwise():
    tim.circle(100, 180)
    tim.setheading(0)
def move_upward():
    tim.setheading(0)
    tim.setheading(90)

def move_down():
    tim.setheading(0)
    tim.setheading(270)


screen.onkeypress(move_forward, "Right")
screen.onkeypress(move_backward, "Left")
screen.onkeypress(move_clockwise, "c")
screen.onkeypress(move, "space")
screen.onkeypress(move_upward,"Up")
screen.onkeypress(move_down,"Down")
screen.listen()
screen.exitonclick()
