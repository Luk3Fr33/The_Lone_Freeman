import turtle


def forw():
    turtle.forward(10) # Values subject to change
    print(turtle.xcor())
    print(turtle.ycor())
    if turtle.xcor() > 330.0:
        turtle.reset()
    elif turtle.xcor() < -330.0:
        turtle.reset()
    elif turtle.ycor() > 270.0:
        turtle.reset()
    elif turtle.ycor() < -270.0:
        turtle.reset()
        
def back():
    turtle.backward(10) # Values sunject to change
    print(turtle.xcor())
    print(turtle.ycor())
    if turtle.xcor() > 330.0:
        turtle.reset()
    elif turtle.xcor() < -330.0:
        turtle.reset()
    elif turtle.ycor() > 270.0:
        turtle.reset()
    elif turtle.ycor() < -270.0:
        turtle.reset()
def left():
    turtle.left(90)    # Values sunject to change

def right():
    turtle.right(90)   # Values sunject to change

turtle.onkeypress(forw, "Up")
turtle.onkeypress(back, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.listen()

turtle.mainloop()
