# Alyssa Mahtani Kaiting
# 230153R
# IT1312

import turtle
import math

# Create a turtle screen with a cyan background
screen = turtle.Screen()
screen.bgcolor("black")
# This turns off screen updates
screen.tracer(0)

# Create a turtle object
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.color("black")
myTurtle.fillcolor("plum")
myTurtle.speed(1)

# Draw a single square of the given size, and fill it in
def drawSquare(t, size):
  """
  Draw a square with the given turtle and size
  """
  t.begin_fill()
  for i in range(4):
    t.forward(size)
    t.left(90)
  t.end_fill()

# Draw a node at the given level, recursively drawing all
# the smaller nodes
def drawNode(t, size, level):
  """
  Draw a node at the given level, recursively drawing all the smaller nodes
  """
  if (level < 1):
    return
  else:
    drawSquare(t, size)

    # Draw the left branch
    leftSize = size * math.sqrt(3) / 2
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.right(150)
    t.forward(leftSize)
    t.left(90)
    drawNode(t, leftSize, level - 1)

    # Draw the right branch
    rightSize = size / 2
    t.right(180)
    t.forward(rightSize)
    t.left(90)
    drawNode(t, rightSize, level - 1)
    t.left(60)
    t.back(size)
# Position the turtle, and start drawing!
myTurtle.penup()
myTurtle.goto(90, -150)
myTurtle.left(90)
myTurtle.pendown()

# Note: 14 levels will take a while to draw!  You can try
# a smaller number, but then the tree won't be as detailed.
drawNode(myTurtle, 80, 14 )

myTurtle.hideturtle()

# Update the screen to see the changes
screen.update()

# Close the turtle graphics window on click
screen.exitonclick()