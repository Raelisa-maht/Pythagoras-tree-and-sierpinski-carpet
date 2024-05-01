# Alyssa Mahtani Kaiting
# 230153R
# IT1312

import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
# This turns off screen updates
screen.tracer(0)

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.color("black")
myTurtle.fillcolor("dark sea green")
myTurtle.speed(1)

# Draw a single square of the given size, and fill it in
def drawSquare(t, size):
  t.begin_fill()
  for i in range(4):
    t.forward(size)
    t.left(90)
  t.end_fill()

# Draw a node at the given level, recursively drawing all
# the smaller nodes
def drawNode(t, size, level):
  if (level < 1):
    return
  else:
    drawSquare(t, size)

    # Draw the left branch
    leftSize = math.sqrt(size * size / 2) # re-computed using Pythagoras formula for balanced tree
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.right(135) # if left-side angle is 45 degrees, this angle is 180-45=135
    t.forward(leftSize)
    t.left(90)
    drawNode(t, leftSize, level - 1)

    # Draw the right branch
    rightSize = math.sqrt(size * size / 2) # re-computed using Pythagoras formula for balanced tree
    t.right(180)
    t.forward(rightSize)
    t.left(90)
    drawNode(t, rightSize, level - 1)
    t.left(45) # if right-side angle is 45 degrees, this angle is = 45
    t.back(size)

# Position the turtle, and start drawing!
myTurtle.penup()
myTurtle.goto(90, -150)
myTurtle.left(90)
myTurtle.pendown()

# Note: 14 levels will take a while to draw!  You can try
# a smaller number, but then the tree won't be as detailed.
drawNode(myTurtle, 80, 14)

myTurtle = turtle.Turtle() # initialization of the module
myWin = turtle.Screen() # initialization of the screen

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen) #move forward
        myTurtle.right(90) # move right with a 90 degree angle
        drawSpiral(myTurtle,lineLen-5) #draw the above movements

drawSpiral(myTurtle,100)
myTurtle.hideturtle()

# Update the screen to see the changes
screen.update()

# Close the turtle graphics window on click
screen.exitonclick()