import turtle

def forw():
    turtle.forward(10) # Values subject to change
    
def back():
    turtle.backward(10) # Values sunject to change
    
def left():
    turtle.left(90)    # Values sunject to change

def right():
    turtle.right(90)   # Values sunject to change

turtle.onkeypress(forw, "Up")
turtle.onkeypress(back, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.listen()
