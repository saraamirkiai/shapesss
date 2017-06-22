from turtle import *
import math

# Name your Turtle. Right now her name is t. If you change her name, make sure to change the name below, too.
sara = Turtle()

# Set Up your screen and starting position.
setup(600,600)
x_pos = -250
y_pos = -150
sara.penup()
sara.setposition(x_pos, y_pos)
sara.pendown()

### Write your code below:
sara.pencolor("pink")
sara.forward(100)
##distance to move
sara.right(90)
##go to the right by 90 degrees
sara.forward(100)
##moving
sara.right(90)
sara.forward(100)
sara.right(90)
sara.forward(100)
sara.right(90)
##square is made
#triangle start
sara.penup()
sara.forward(300)
sara.pendown()
sara.forward(200)
sara.left(120)
sara.forward(200)
sara.left(120)
sara.forward(200)
sara.penup()
sara.right (100)
sara.forward(10)
sara.pendown()
sara.forward(300)
sara.right(10)







# Close window on click.
exitonclick()
