# Alyssa Mahtani Kaiting
# 230153R
# IT1312

import turtle

def drawTriangle(points, myTurtle, color):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()

def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, myTurtle):
    color_map = ['blue', 'red', 'green', 'cyan', 'yellow', 'magenta']  # Add more colors if needed

    drawTriangle(points, myTurtle, color_map[degree])

    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree-1, myTurtle)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(10)
    myWin = turtle.Screen()

    myPoints = [[-200, -50], [0, 200], [200, -50]]
    degree = 5

    sierpinski(myPoints, degree, myTurtle)

    myTurtle.hideturtle()
    myWin.exitonclick()

if __name__ == "__main__":
    main()
