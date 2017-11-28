"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Christopher Fusaro.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(15)    # Delay to slow down animations.

# The radius of the first circle will 40:
radius = 40

# The first square will be 300 x 300 pixels:
size = 80

orange_turtle = rg.SimpleTurtle("turtle")
orange_turtle.pen = rg.Pen("orange", 10)    # Use an orange pen.

# Repeat the loop four times.
for i in range(4):

    # Draw a circle of a given radius.
    orange_turtle.draw_circle(radius)

    # Pick the pen up, stop drawing, and move backwards.
    orange_turtle.pen_up()
    orange_turtle.backward(15)

    # Put the pen down and decrease the stored radius value.
    orange_turtle.pen_down()
    radius = radius - 5

# Introduce a new turtle.
green_turtle = rg.SimpleTurtle("turtle")

# Move the turtle forward.
green_turtle.forward(50)
green_turtle.pen = rg.Pen("green", 5)   # Uses a green pen.
green_turtle.speed = 500    # Speed of the turtle.

# Run the embeded code four times.
for k in range(4):

    # Draw a square with diimensions of the stored size
    green_turtle.draw_square(size)

    # Pick the pen up, stop drawing, and move forward.
    green_turtle.pen_up()
    green_turtle.forward(20)

    # Put the pen down and decrease the dimensions of the square.
    green_turtle.pen_down()
    size = size - 5


window.close_on_mouse_click()