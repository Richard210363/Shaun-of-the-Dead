#Imports
import turtle
import math
import random
import time

#Define the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Shaun of the Dead v08")
wn.setup(700,700)

#Prepare assets
turtle.register_shape("Zombie.gif")        #new
turtle.register_shape("Left_Facing_Zombie.gif")
turtle.register_shape("Right_Facing_Zombie.gif")
turtle.register_shape("Shaun.gif")
turtle.register_shape("Left_Facing_Shaun.gif")        #new
turtle.register_shape("Right_Facing_Shaun.gif")
turtle.register_shape("Wall.gif")
turtle.register_shape("Gun.gif")

#Define Walls
class WallBlock(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Wall.gif") 
        self.penup()
        self.speed(0)
        self.shapesize(2,2,2)
        turtle.resizemode("user")

#Define Player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Shaun.gif")
        self.penup()
        self.speed(0)
        self.bullets=0

    #Define Player Movement
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
    
    #Define Player Events            
    def is_collision(self, other):
        a=self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance < 1:
            return True
        else:
            return False

#Define Treasure
class Treasure(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Gun.gif")
        self.penup()
        self.speed(0)
        self.bullets = 100

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

#Define Enemies
class Enemy(turtle.Turtle):         #new
  def __init__(self, x, y):
    turtle.Turtle.__init__(self)
    self.shape('Zombie.gif')
    self.penup()
    self.speed(0)
    self.gold = 25
    self.goto(x, y)
    self.direction = random.choice(['up', 'down', 'left', 'right'])
   
  #Set direction parameters
  def move(self):
    if self.direction == 'up':
      dx = 0
      dy = 24
      self.shape('Zombie.gif')
    elif self.direction == 'down':
      dx = 0
      dy = -24
      self.shape('Zombie.gif')
    elif self.direction == 'left':
      dx = -24
      dy = 0
      self.shape('Left_Facing_Zombie.gif')
    elif self.direction == 'right':
      dx = 24
      dy = 0
      self.shape('Right_Facing_Zombie.gif')
    else:
      dx = 0
      dy = 0
      self.shape('Zombie.gif')

    #Define Movement
    move_to_x = self.xcor() + dx
    move_to_y = self.ycor() + dy

    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)
    else:
      self.direction = random.choice(['up', 'down', 'left', 'right'])

    #Set timer event
    turtle.ontimer(self.move, t=random.randint(100, 500))

#Define Level 1
level_1 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "X  XXXXXXX          XXXXX",
            "X  XXXXXXX  XXXXXX  XXXXX",
            "X  P   XX  XXXXXX  XXXXX",
            "X       XX  XXX        XX",
            "XXXXXX  XX  XXX E      XX",
            "XXXXXX  XX  XXXXXX  XXXXX",
            "XXXXXX  XX    XXXX  XXXXX",
            "X  XXX        XXXX TXXXXX",
            "X  XXX   XXXXXXXXXXXXXXXX",
            "X         XXXXXXXXXXXXXXX",
            "X      X   E     XXXXXXXX",
            "XXXXXXXXXXXX     XXXXX  X",
            "XXXXXXXXXXXXXXX  XXXXX  X",
            "XXX  XXXXXXXXXX         X",
            "XXX                     X",
            "XXX         XXXXXXXXXXXXX",
            "XXXXXXXXXX  XXXXXXXXXXXXX",
            "XXXXXXXXXX              X",
            "XX   XXXXX     E        X",
            "XX   XXXXXXXXXXXXX  XXXXX",
            "XX    XXXXXXXXXXXX  XXXXX",
            "XX           XXXX       X",
            "XXXX                    X",
            "XXXXXXXXXXXXXXXXXXXXXXXXX"
           ]

#Define creating a level
def setup_level(level):
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

            if character == 'E':
                enemies.append(Enemy(screen_x, screen_y))

#Create items from classes
wallBlock = WallBlock()
player = Player()
treasure = Treasure()

#Create Lists
enemies = []
walls = []

#Create level and start game
setup_level(level_1)

#Start timer
for enemy in enemies:
  turtle.ontimer(enemy.move, t=250)         #new

#Listen to kjeyboard input
turtle.listen()
turtle.onkey(player.go_left,"a")
turtle.onkey(player.go_right,'d')
turtle.onkey(player.go_up,'w')
turtle.onkey(player.go_down,'s')
wn.tracer(0)

# Main game loop
while True:
    for enemy in enemies:            #new
        if player.is_collision(enemy):
            print ("Shaun is DEAD!!")
    if player.is_collision(treasure):
        player.bullets += treasure.bullets
        print ("Shaun got {} bullets".format(treasure.bullets)) 
        print ("Shaun has got {} bullets".format(player.bullets))
        treasure.destroy()
    wn.update()