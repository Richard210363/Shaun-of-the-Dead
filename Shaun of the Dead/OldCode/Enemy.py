#Imports
import turtle
import math
import random
import datetime
import WallBlock

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('Zombie.gif')
        self.color('orange')
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        self.can_kill = True
        self.then_move=datetime.datetime.now() #NB: We don't actually need the word self here.  Self is assumed because we're inside the class at this point
        self.name = "Zombie " + str(random.random())
        self.then_collision=datetime.datetime.now()
        self.closeFlag = False

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
 
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

        now_collision=datetime.datetime.now()      
        diff_collision = now_collision - self.then_collision

        #print("Difference:", diff)
        #print("Days:", diff.days)
        #print("Microseconds:", diff.microseconds)
        #print("Seconds:", diff.seconds)

        if diff_move.microseconds<200000:  # Set Enemy speed here. Lower is faster
            return

        self.then_move=now_move

#Is a player close enough to interact with        
        if diff_collision.microseconds>5000000:        
            self.closeFlag = False
            if self.is_close(player):
                if player.xcor() < self.xcor():
                    self.direction = 'left'
                if player.xcor() > self.xcor():
                    self.direction = 'right'
                if player.ycor() < self.ycor():
                    self.direction = 'down'
                if player.ycor() > self.ycor():
                    self.direction = 'up'
                self.closeFlag = True




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
            #print (self.name + " move_to_x = " + str(move_to_x))
            #print (self.name + " move_to_y = " + str(move_to_y))
            self.goto(move_to_x, move_to_y)
        #else:
            #print (self.name + " can't move into walls")

#Set direction for next iteration
        if self.closeFlag == False:
            self.direction = random.choice(['up', 'down', 'left', 'right'])

#Have we hit a player
#Enemies must leave a player before they can be hit again 
    def is_collision_with_player(self, other):
        a=self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance > 10:
            self.can_kill=True
            #print ("Distance > 10")
            #print (distance)

        if self.can_kill:
            if distance < 5:
                self.then_collision=datetime.datetime.now() 
                self.can_kill=False
                #print ("Distance < 5")
                #print (distance)
                return True
            else:
                return False



#The Original Code
#class Enemy(turtle.Turtle):
#    def __init__(self, x, y):
#        turtle.Turtle.__init__(self)
#        self.shape('Zombie.gif')
#        self.color('orange')
#        self.penup()
#        self.speed(0)
#        self.gold = 25
#        self.goto(x, y)
#        self.direction = random.choice(['up', 'down', 'left', 'right'])
#        self.can_kill = True

#    def destroy(self):
#        self.goto(2000,2000)
#        self.hideturtle()
 
#    #Is the player close?
#    def is_close(self, other):
#        a = self.xcor()-other.xcor()
#        b = self.ycor()-other.ycor()
       
#        distance = math.sqrt((a ** 2) + (b ** 2) )
#        if distance < 150:
#            return True
#        else:
#            return False

#    #Set direction parameters
#    def move(self):
#        if self.direction == 'up':
#          dx = 0
#          dy = 24
#          self.shape('Zombie.gif')
#        elif self.direction == 'down':
#          dx = 0
#          dy = -24
#          self.shape('Zombie.gif')
#        elif self.direction == 'left':
#          dx = -24
#          dy = 0
#          self.shape('Left_Facing_Zombie.gif')
#        elif self.direction == 'right':
#          dx = 24
#          dy = 0
#          self.shape('Right_Facing_Zombie.gif')
#        else:
#          dx = 0
#          dy = 0
#          self.shape('Zombie.gif')

#        closeFlag = False
     
#        if self.is_close(player):
#            if player.xcor() < self.xcor():
#                self.direction = 'left'
#            if player.xcor() > self.xcor():
#                self.direction = 'right'
#            if player.ycor() < self.ycor():
#                self.direction = 'down'
#            if player.ycor() > self.ycor():
#                self.direction = 'up'
#            closeFlag = True

#        #Define Movement
#        move_to_x = self.xcor() + dx
#        move_to_y = self.ycor() + dy

#        if (move_to_x, move_to_y) not in walls:
#            self.goto(move_to_x, move_to_y)
#        elif closeFlag == False:
#            self.direction = random.choice(['up', 'down', 'left', 'right'])

#        #Set timer event
#        turtle.ontimer(self.move, t=random.randint(100, 300))

#    def is_collision_with_player(self, other):
#        a=self.xcor() - other.xcor()
#        b = self.ycor() - other.ycor()
#        distance = math.sqrt((a **2) + (b **2))

#        if distance > 10:
#            self.can_kill=True
#            #print ("Distance > 10")
#            #print (distance)

#        if self.can_kill:
#            if distance < 5:
#                self.can_kill=False
#                #print ("Distance < 5")
#                #print (distance)
#                return True
#            else:
#                return False