from turtle import Turtle, Screen

brush = Turtle()
screen = Screen()

def move_forward():
  brush.forward(10)

def move_backward():
  brush.back(10)

def turn_right():
  brush.right(10)

def turn_left():
  brush.left(10)

def clear():
  brush.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
