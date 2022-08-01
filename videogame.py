import turtle
turtle.textinput('Lone Freeman', 'Welcome to the Lone Freeman! Press enter to start.')

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
    obst(turtle,xpositions, ypositions)
    
def back():
    turtle.backward(10) # Values subject to change
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
    obst(turtle,xpositions, ypositions)
   
def left():
    turtle.left(90)    # Values subject to change

def right():
    turtle.right(90)   # Values subject to change


    
turtle.onkeypress(forw, "Up")
turtle.onkeypress(back, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

turtle.listen()

turtle.bgcolor("red")




xpositions = []
ypositions = []    

dist = 200
for i in range(5):
        
    tur1 = turtle.Turtle()
        
    tur1.shape('triangle')
        
    tur1.penup()
    tur1.goto(0,0)
    tur1.forward(dist)
    tur1.left(90)
    tur1.pendown()
    xpositions.append(tur1.xcor())
    ypositions.append(tur1.ycor())
    print(xpositions)
    print(ypositions)
    dist = dist + 100  
def obst(turtle,xpositions, ypositions):
    
  
   
    x = 0
    
    for i in xpositions:
        print(int(xpositions[x]) - int(turtle.xcor()))
        if int(xpositions[x]) - int(turtle.xcor()) <= abs(1) and int(ypositions[x]) - int(turtle.ycor()) <= abs(1):
            turtle.reset()
            

            
        x = x + 1
    
    
    
    
    


turtle.mainloop()

