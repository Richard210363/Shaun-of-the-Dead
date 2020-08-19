import turtle

#Define Walls
class WallBlock(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Resources\\Wall.gif")
        self.penup()
        self.speed(0)
        self.shapesize(2,2,2)
        turtle.resizemode("user")