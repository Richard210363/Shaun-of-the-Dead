import turtle
import math
import random
import datetime

import Entities.wall_block as wall_block
import DataManagement.game_state_manager as game_state_manager
import AIManagement.NPC_AI as NPC_AI

class NPC(turtle.Turtle):
    def __init__(self, x, y, bullets, name, lives, gameStateManager, npc_list):
        turtle.Turtle.__init__(self)
        self.x_cor=x
        self.y_cor=y
        self.name=name        
        self.bullets=bullets      
        self.lives=lives
        self.shape("A")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.direction="go_down"
        self.can_get_bullets=True
        self.can_get_lives=True
        self.walls = []
        self.gameStateManager=gameStateManager
        self.then_move=datetime.datetime.now()
        self.NPC_AI = NPC_AI.NPC_AI()

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

#Move sprite
    def move(self, walls, player): #do we really want to pass the player to an NPC?

#Set the speed of NPC movement by not moving in too short a time period
        now_move=datetime.datetime.now()      
        diff_move = now_move - self.then_move

        if diff_move.microseconds<300000:  # Set NPC speed here. Lower is faster
            return

        self.then_move=now_move

#Calculate direction
        self.NPC_AI.get_direction_searching(self, player)

#Set sprite picture and movement deltas
        if self.direction == 'go_up':
          dx = 0
          dy = 24
          self.shape("Zombie.gif")
        elif self.direction == 'go_down':
          dx = 0
          dy = -24
          self.shape("Zombie.gif")
        elif self.direction == 'go_left':
          dx = -24
          dy = 0
          self.shape("Left_Facing_Zombie.gif")
        elif self.direction == 'go_right':
          dx = 24
          dy = 0
          self.shape("Right_Facing_Zombie.gif")
        else:
          dx = 0
          dy = 0
          self.shape("Zombie.gif")

#Move
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            self.x_cor = move_to_x
            self.y_cor = move_to_y
            if self.NPC_AI.found_Shaun(self, player):
                print("Found Shaun")

##Set direction for next iteration
#        self.direction = self.NPC_AI.get_direction_random()

        pass

        pass