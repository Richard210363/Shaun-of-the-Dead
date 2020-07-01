import turtle

#Define base treasure class
class Treasure(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()



#Define Treasure_Bullets
class Treasure_Bullets(Treasure):
    def __init__(self):
        super().__init__()
        self.shape("Gun.gif")
        self.bullets = 10

    def GetBullets(self, treasure_type):
        if treasure_type == "UnLimited":
            return 1
        if treasure_type == "Limited":
            if self.bullets >0:
                self.bullets -=1
                return 1
            else:
                self.destroy()
                return 0


#Define Treasure_Lives
class Treasure_Lives(Treasure):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.lives = 1
