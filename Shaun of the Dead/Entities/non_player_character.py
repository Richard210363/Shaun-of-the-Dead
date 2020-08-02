import turtle
import math
import random
import datetime

import Entities.wall_block as wall_block
import DataManagement.game_state_manager as game_state_manager
import AIManagement.NPC_movement as NPC_movement

class NPC(turtle.Turtle):
    def __init__(self, x, y, bullets, name, lives, gameStateManager, npc_list):
        turtle.Turtle.__init__(self)
        self.x_cor=x
        self.y_cor=y
        self.name=name        
        self.bullets=bullets      
        self.lives=lives
        self.shape("Shaun.gif")
        self.color("blue")
        self.penup()
        #self.speed(0)
        #self.direction=""
        self.can_get_bullets=True
        self.can_get_lives=True
        #self.walls = []
        self.gameStateManager=gameStateManager
        #self.then_move=datetime.datetime.now()
        #self.then_collision=datetime.datetime.now()
        #self.closeFlag = False
        #self.can_chase = True
        self.NPC_movement = NPC_movement.NPC_movement()

       #Define NPC Events   
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

    def move(self, walls): 
        self.NPC_movement.move(walls)

        if self.NPC_movement.direction == 'up':
          dx = 0
          dy = 24
          self.shape("Shaun.gif")
        elif self.NPC_movement.direction == 'down':
          dx = 0
          dy = -24
          self.shape("Shaun.gif")
        elif self.NPC_movement.direction == 'left':
          dx = -24
          dy = 0
          self.shape("Left_Facing_Shaun.gif")
        elif self.NPC_movement.direction == 'right':
          dx = 24
          dy = 0
          self.shape('Right_Facing_Shaun.gif')
        else:
          dx = 0
          dy = 0
          self.shape("Shaun.gif")

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:

            self.goto(move_to_x, move_to_y)