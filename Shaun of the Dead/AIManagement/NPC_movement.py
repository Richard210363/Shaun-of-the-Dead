import math
import random
import datetime

class NPC_movement(object):
    """description of class"""
    def __init__(self):
        #self.speed(0)
        self.direction=""
        self.then_move=datetime.datetime.now()
        self.then_collision=datetime.datetime.now()
        self.closeFlag = False
        self.can_chase = True

#Move sprite
    def move(self, walls): #do we really want to pass the player to an NPC?

#Set the speed of NPC movement by not moving in too short a time period
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

        if diff_move.microseconds<300000:  # Set NPC speed here. Lower is faster
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


##Set sprite picture and movement deltas
#        if self.direction == 'up':
#          dx = 0
#          dy = 24
#          self.shape("Shaun.gif")
#        elif self.direction == 'down':
#          dx = 0
#          dy = -24
#          self.shape("Shaun.gif")
#        elif self.direction == 'left':
#          dx = -24
#          dy = 0
#          self.shape("Left_Facing_Shaun.gif")
#        elif self.direction == 'right':
#          dx = 24
#          dy = 0
#          self.shape('Right_Facing_Shaun.gif')
#        else:
#          dx = 0
#          dy = 0
#          self.shape("Shaun.gif")

#Move
        #move_to_x = self.xcor() + dx
        #move_to_y = self.ycor() + dy

        #if (move_to_x, move_to_y) not in walls:

        #    self.goto(move_to_x, move_to_y)


#Set direction for next iteration
        if self.closeFlag == False:
            self.direction = random.choice(['up', 'down', 'left', 'right'])