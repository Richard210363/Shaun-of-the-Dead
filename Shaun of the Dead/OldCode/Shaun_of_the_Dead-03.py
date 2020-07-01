
import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Shaun of the Dead v03")
wn.setup(700,700)



class WallBlock(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        #self.penup()
        self.speed(0)

    def go_up(self):      #NEW
        self.goto(self.xcor(),self.ycor()+24)
   
    def go_down(self):
        self.goto(self.xcor(),self.ycor()+24)

    def go_left(self):
        self.goto(self.xcor()-24,self.ycor())
   
    def go_right(self):
        self.goto(self.xcor()+24,self.ycor())

level_1 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "X  XXXXXXX          XXXXX",
            "X  XXXXXXX  XXXXXX  XXXXX",
            "X  P    XX  XXXXXX  XXXXX",
            "X       XX  XXX        XX",
            "XXXXXX  XX  XXX        XX",
            "XXXXXX  XX  XXXXXX  XXXXX",
            "XXXXXX  XX    XXXX  XXXXX",
            "X  XXX        XXXX  XXXXX",
            "X  XXX  XXXXXXXXXXXXXXXXX",
            "X         XXXXXXXXXXXXXXX",
            "X                XXXXXXXX",
            "XXXXXXXXXXXX     XXXXX  X",
            "XXXXXXXXXXXXXXX  XXXXX  X",
            "XXX  XXXXXXXXXX         X",
            "XXX                     X",
            "XXX         XXXXXXXXXXXXX",
            "XXXXXXXXXX  XXXXXXXXXXXXX",
            "XXXXXXXXXX              X",
            "XX   XXXXX              X",
            "XX   XXXXXXXXXXXXX  XXXXX",
            "XX    XXXXXXXXXXXX  XXXXX",
            "XX           XXXX       X",
            "XXXX                    X",
            "XXXXXXXXXXXXXXXXXXXXXXXXX"
           ]


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                wallBlock.goto(screen_x, screen_y)
                wallBlock.stamp()

            if character == "P":
                player.goto(screen_x, screen_y)


wallBlock = WallBlock()
player = Player()

setup_maze(level_1)

turtle.listen()      #NEW
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,'Right')
turtle.onkey(player.go_up,'Up')
turtle.onkey(player.go_down,'Down')

while True:
    wn.update()      #NEW