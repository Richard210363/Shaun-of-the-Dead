import turtle
import math
import random
import datetime

import Entities.wall_block as wall_block
import DataManagement.game_state_manager as game_state_manager
#import ListManagement.enemy_list as enemy_list

class Enemy(turtle.Turtle):
    def __init__(self, x, y, type, name, lives, gameStateManager, enemy_list):
        turtle.Turtle.__init__(self)
        self.shape('Zombie.gif')
        self.color('orange')
        self.penup()
        self.speed(0)
        self.gold = 25
        #self.goto(x, y)
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        self.can_kill = True
        self.then_move=datetime.datetime.now() #NB: We don't actually need the word self here.  Self is assumed because we're inside the class at this point
        self.name = name
        self.then_collision=datetime.datetime.now()
        self.closeFlag = False
        self.can_chase = True
        self.lives=lives
        self.type=type
        self.x_cor=x
        self.y_cor=y
        self.gameStateManager=gameStateManager
        #self.gameStateManager.appendZombie(self.name) #new
        self.enemy_list=enemy_list

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

    def wound(self):
        self.lives -=1
        if self.lives <= 0:
            self.destroy()
            print ("Shaun killed a zombie!")
            self.enemy_list.remove_enemy_from_list(self)
        self.gameStateManager.updateZombie(self.name,self.lives)

 
#Is the player close to self?  Triggers the hunting response
    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
       
        distance = math.sqrt((a ** 2) + (b ** 2) )
        if distance < 150:
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

#Is a player close enough to interact with        
        if self.can_chase==True:
            print("Can Chase Shaun")
            self.closeFlag = False
            if self.is_close(player):
                print("Chasing Shaun")
                if player.xcor() < self.xcor():
                    self.direction = 'left'
                if player.xcor() > self.xcor():
                    self.direction = 'right'
                if player.ycor() < self.ycor():
                    self.direction = 'down'
                if player.ycor() > self.ycor():
                    self.direction = 'up'
                self.closeFlag = True
        else:
            print("Can't Chase Shaun Yet")


#Set sprite picture and movement deltas
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

#Move
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:

            self.goto(move_to_x, move_to_y)


#Set direction for next iteration
        if self.closeFlag == False:
            self.direction = random.choice(['up', 'down', 'left', 'right'])

#Have we hit a player?
#Enemies must leave a player before they can be hit again 
    def is_collision_with_player(self, other):
        a=self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance > 10:
            self.can_kill=True

        if self.can_kill:
            if distance < 5:
                self.can_chase = False
                self.then_collision=datetime.datetime.now() 
                self.can_kill=False

                return True
            else:
                return False
