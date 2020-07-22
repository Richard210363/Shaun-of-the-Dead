import turtle
import math
import random
import datetime

import Entities.wall_block as wall_block
import DataManagement.game_state_manager as game_state_manager

class NPC(turtle.Turtle):
    def __init__(self, x, y, bullets, name, lives, gameStateManager, npc_list):
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

#Move sprite
    def move(self,player,walls):

#Set the speed of Enemy movement by not moving in too short a time period
        now_move=datetime.datetime.now()      
        diff_move = now_move - self.then_move

#Determine how long it is since the last collision
        now_collision=datetime.datetime.now()      
        diff_collision = now_collision - self.then_collision

#Set the can chase flag based on how long its been since a collision
        if self.can_chase==False:
            if diff_collision.seconds>2:
                self.can_chase=True


        #print("Difference:", diff)
        #print("Days:", diff.days)
        #print("Microseconds:", diff.microseconds)
        #print("Seconds:", diff.seconds)

        if diff_move.microseconds<300000:  # Set Enemy speed here. Lower is faster
            return

        self.then_move=now_move

##Is a player close enough to interact with        
#        if self.can_chase==True:
#            print("Can Chase Shaun")
#            self.closeFlag = False
#            if self.is_close(player):
#                print("Chasing Shaun")
#                if player.xcor() < self.xcor():
#                    self.direction = 'left'
#                if player.xcor() > self.xcor():
#                    self.direction = 'right'
#                if player.ycor() < self.ycor():
#                    self.direction = 'down'
#                if player.ycor() > self.ycor():
#                    self.direction = 'up'
#                self.closeFlag = True
#        else:
#            print("Can't Chase Shaun Yet")


#Set sprite picture and movement deltas
        if self.direction == 'up':
          dx = 0
          dy = 24
          self.shape("Shaun.gif")
        elif self.direction == 'down':
          dx = 0
          dy = -24
          self.shape("Shaun.gif")
        elif self.direction == 'left':
          dx = -24
          dy = 0
          self.shape("Left_Facing_Shaun.gif")
        elif self.direction == 'right':
          dx = 24
          dy = 0
          self.shape('Right_Facing_Shaun.gif')
        else:
          dx = 0
          dy = 0
          self.shape("Shaun.gif")

#Move
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:

            self.goto(move_to_x, move_to_y)


#Set direction for next iteration
        if self.closeFlag == False:
            self.direction = random.choice(['up', 'down', 'left', 'right'])