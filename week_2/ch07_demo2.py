# Topic : turtle , random Modules
# DEMO

import turtle
import random as random

# let's check turtle's documentation

# turtle.forward(100) # forward 100 pixls
# turtle.left(120)   # turn 120 deg clockwise
# turtle.forward(100)


turtle.shape("turtle")
def drawCircle(x, y):
    """
    # Draw a circle there , and fill it with
    # a random color .
    """
    turtle.penup()
    turtle.fillcolor(random.random(), random.random(), random.random()) # Red Green Blue
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()

turtle.title ("Click on the canvas !")

# bind left mouse button to drawCircle function
turtle.onscreenclick(drawCircle)
#
#
#
# # Initiate main loop
turtle.mainloop()
#
#
