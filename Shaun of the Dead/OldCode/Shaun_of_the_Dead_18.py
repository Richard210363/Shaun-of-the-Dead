class Shaun_of_the_Dead_18(object):
    """description of class"""


#Imports
import turtle
import math

#Prepare assets
turtle.register_shape("Zombie.gif")
turtle.register_shape("Left_Facing_Zombie.gif")
turtle.register_shape("Right_Facing_Zombie.gif")
turtle.register_shape("Shaun.gif")
turtle.register_shape("Left_Facing_Shaun.gif")
turtle.register_shape("Right_Facing_Shaun.gif")
turtle.register_shape("Wall.gif")
turtle.register_shape("Gun.gif")

#Define the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Shaun of the Dead v18")
wn.setup(700,700)

#Define what to do when we fire a bullet
def fire_bullet():
    if player.bullets > 0:
        player.bullets -= 1
        print ("Shaun has " + str(player.bullets) + " bullets remaining")
        bullet = Bullet()
        bullets.append(bullet)
        bullet.set_direction()
    if player.bullets == 0:
        print ("Shaun has no bullets")

def moveEnemies():
    for enemy in enemies:
        enemy.move(player,walls)
      
##Define Walls
#class WallBlock(turtle.Turtle):
#    def __init__(self):
#        turtle.Turtle.__init__(self)
#        self.shape("Wall.gif")
#        self.penup()
#        self.speed(0)
#        self.shapesize(2,2,2)
#        turtle.resizemode("user")

##Define Player
#class Player(turtle.Turtle):
#    def __init__(self):
#        turtle.Turtle.__init__(self)
#        self.shape("Shaun.gif")
#        self.color("blue")
#        self.penup()
#        self.speed(0)
#        self.bullets=10
#        self.direction=""
#        self.can_get_bullets=True
#        self.lives=5
#        self.can_get_lives=True

#    #Define Player Movement
#    def go_up(self):
#        move_to_x = self.xcor()
#        move_to_y = self.ycor()+24
#        if(move_to_x,move_to_y) not in walls:
#            self.goto(move_to_x,move_to_y)
#            self.shape("Shaun.gif")
#            self.direction="go_up"

#    def go_down(self):
#        move_to_x = self.xcor()
#        move_to_y = self.ycor()-24
#        if(move_to_x,move_to_y) not in walls:
#            self.goto(move_to_x,move_to_y)
#            self.shape("Shaun.gif")
#            self.direction="go_down"

#    def go_left(self):
#        move_to_x = self.xcor()-24
#        move_to_y = self.ycor()
#        if(move_to_x,move_to_y) not in walls:
#            self.goto(move_to_x,move_to_y)
#            self.shape("Left_Facing_Shaun.gif")
#            self.direction="go_left"

#    def go_right(self):
#        move_to_x = self.xcor()+24
#        move_to_y = self.ycor()
#        if(move_to_x,move_to_y) not in walls:
#            self.goto(move_to_x,move_to_y)
#            self.shape("Right_Facing_Shaun.gif")
#            self.direction="go_right"
   
#    #Define Player Events            
#    def is_collision_with_treasure(self, other):
#        a=self.xcor() - other.xcor()
#        b = self.ycor() - other.ycor()
#        distance = math.sqrt((a **2) + (b **2))

#        if distance > 10:
#            self.can_get_bullets=True
#            #print ("Distance > 10")
#            #print (distance)

#        if self.can_get_bullets:
#            if distance < 5:
#                self.can_get_bullets=False
#                #print ("Distance < 5")
#                #print (distance)
#                return True
#            else:
#                return False

#    def is_collision_with_treasure_lives(self, other):
#        a=self.xcor() - other.xcor()
#        b = self.ycor() - other.ycor()
#        distance = math.sqrt((a **2) + (b **2))

#        if distance > 10:
#            self.can_get_lives=True
#            #print ("Distance > 10")
#            #print (distance)

#        if self.can_get_lives:
#            if distance < 5:
#                self.can_get_lives=False
#                #print ("Distance < 5")
#                #print (distance)
#                return True
#            else:
#                return False

#Define Treasure
class Treasure(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Gun.gif")
        self.penup()
        self.speed(0)
        self.bullets = 10

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

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
class Treasure_Lives(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
        self.lives = 1

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


#Define Bullet
class Bullet(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.direction = ""

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

    #Define Bullet Movement
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("circle")
        if(move_to_x,move_to_y) in walls:
            self.destroy()
   
    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("circle")
        if(move_to_x,move_to_y) in walls:
            self.destroy()

    def go_left(self):
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("circle")
        if(move_to_x,move_to_y) in walls:
            self.destroy()
   
    def go_right(self):
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("circle")
        if(move_to_x,move_to_y) in walls:
            self.destroy()

    def move(self):
        if(self.direction=="go_up"):
            self.go_up()
        if(self.direction=="go_down"):
            self.go_down()
        if(self.direction=="go_left"):
            self.go_left()
        if(self.direction=="go_right"):
            self.go_right()
           
        #Set timer event
        turtle.ontimer(self.move, t=250)

    def set_direction(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor()
        self.goto(move_to_x,move_to_y)
        if(player.direction=="go_up"):
            self.direction="go_up"
        if(player.direction=="go_down"):
            self.direction="go_down"
        if(player.direction=="go_left"):
            self.direction="go_left"
        if(player.direction=="go_right"):
            self.direction="go_right"
        self.move()

    def is_collision(self, enemy):
        a=self.xcor() - enemy.xcor()
        b = self.ycor() - enemy.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance < 5:
            return True
        else:
            return False

#Define Level 1
level_1 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "X  XXXXXXX          XXXXX",
            "X  XXXXXXX  XXXXXX  XXXXX",
            "X  P  T XX  XXXXXX  XXXXX",
            "X    L  XX  XXX        XX",
            "XXXXXX  XX  XXX E      XX",
            "XXXXXX  XX  XXXXXX  XXXXX",
            "XXXXXX  XX    XXXX  XXXXX",
            "X  XXX        XXXX  XXXXX",
            "X  XXX  XXXXXXXXXXXXXXXXX",
            "X         XXXXXXXXXXXXXXX",
            "X          E     XXXXXXXX",
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
                enemies.append(Enemy.Enemy(screen_x, screen_y))

            if character == "L":
                treasure_lives.goto(screen_x, screen_y)
           

#Everything above line this is preparing objects
###############################
#Everything below line this is the program that does things

#Create items from classes
wallBlock = WallBlock.WallBlock()
player = Player.Player()
treasure = Treasure()
treasure_lives = Treasure_Lives()

#Create Lists
enemies = []
walls = []
bullets = []

player.walls = walls

#Create level and start game
setup_level(level_1)

#Listen to keyboard input
turtle.listen()
turtle.onkey(player.go_left,"a")
turtle.onkey(player.go_right,'d')
turtle.onkey(player.go_up,'w')
turtle.onkey(player.go_down,'s')
turtle.onkey(fire_bullet,'f')
wn.tracer(0)

# Main game loop
while True:

    for enemy in enemies:
        if enemy.is_collision_with_player(player):
            player.lives -=1
            if player.lives <= 0:
                print ("Shaun is DEAD!!")
            else:
                print ("Shaun has lost a life!!")
                print ("Shaun has got " + str(player.lives) + " lives remaining")

        for bullet in bullets:
            if bullet.is_collision(enemy):
                bullet.destroy()
                enemy.destroy()

    if player.is_collision_with_treasure(treasure):

        player.bullets += treasure.GetBullets("Limited")

        print ("Shaun has " + str(player.bullets) + " bullets")
        #treasure.destroy()

    if player.is_collision_with_treasure_lives(treasure_lives):
        player.lives += treasure_lives.lives
        print ("Shaun has gained a life")
        print ("Shaun has " + str(player.lives) + " lives")
        #treasure_lives.destroy()

    moveEnemies()
    wn.update()
