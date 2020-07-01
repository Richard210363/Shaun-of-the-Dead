
import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Shaun of the Dead v07")
wn.setup(700,700)   #new

turtle.register_shape("Left_Facing_Shaun.gif")        #new
turtle.register_shape("Right_Facing_Shaun.gif")
turtle.register_shape("Shaun.gif")
turtle.register_shape("Wall.gif")
turtle.register_shape("Gun.gif")

class WallBlock(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Wall.gif")          #new
        self.penup()
        self.speed(0)
        self.shapesize(2,2,2)     #new
        turtle.resizemode("user")

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Shaun.gif")     #new
        self.penup()
        self.speed(0)
        self.bullets = 100

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Shaun.gif")

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Shaun.gif")

    def go_left(self):
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Left_Facing_Shaun.gif")
   
    def go_right(self):
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Right_Facing_Shaun.gif")

    def is_collision(self, other):
        a=self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distence = math.sqrt((a **2) + (b **2))

        if distence < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Gun.gif")
        self.penup()
        self.speed(0)
        self.bullets = 110

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


level_1 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "X  XXXXXXX          XXXXX",
            "X  XXXXXXX  XXXXXX  XXXXX",
            "X  P   TXX  XXXXXX  XXXXX",
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
                walls.append((screen_x,screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasure.goto(screen_x, screen_y)


wallBlock = WallBlock()
player = Player()
treasure = Treasure()

walls = []

setup_maze(level_1)

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,'Right')
turtle.onkey(player.go_up,'Up')
turtle.onkey(player.go_down,'Down')

# Main game loop
while True:
    if player.is_collision(treasure):
        player.bullets += treasure.bullets
        print ("Shaun got {} bullets".format(treasure.bullets)) 
        print ("Shaun has got {} bullets".format(player.bullets))
        treasure.destroy()
    wn.update()