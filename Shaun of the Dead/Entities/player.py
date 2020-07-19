import turtle
import math
import random
import datetime

import Entities.wall_block as wall_block
import DataManagement.game_state_manager as game_state_manager

class Player(turtle.Turtle):
    def __init__(self, x, y, bullets, name, lives, gameStateManager, player_list):
        turtle.Turtle.__init__(self)
        self.shape("Shaun.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.bullets=bullets
        self.direction=""
        self.can_get_bullets=True
        self.lives=lives
        self.can_get_lives=True
        self.walls = []
        self.gameStateManager=gameStateManager
        self.x_cor=x
        self.y_cor=y
        self.name=name
        #gameStateManager.set("name" , "Shaun") #new
        

    #Define Player Movement
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()+24
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Shaun.gif")
            self.direction="go_up"

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Shaun.gif")
            self.direction="go_down"

    def go_left(self):
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Left_Facing_Shaun.gif")
            self.direction="go_left"

    def go_right(self):
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()
        if(move_to_x,move_to_y) not in self.walls:
            self.goto(move_to_x,move_to_y)
            self.shape("Right_Facing_Shaun.gif")
            self.direction="go_right"
   
    #Define Player Events   
    # def is_collision_with_treasure_bullets(self, other):         
    def is_collision_with_treasure_bullets(self, other):
        a=self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance > 10:
            self.can_get_bullets=True
            #print ("Distance > 10")
            #print (distance)

        if self.can_get_bullets:
            if distance < 5:
                self.can_get_bullets=False
                #print ("Distance < 5")
                #print (distance)
                return True
            else:
                return False

    def is_collision_with_treasure_lives(self, other):
        a=self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance > 10:
            self.can_get_lives=True
            #print ("Distance > 10")
            #print (distance)

        if self.can_get_lives:
            if distance < 5:
                self.can_get_lives=False
                #print ("Distance < 5")
                #print (distance)
                return True
            else:
                return False
