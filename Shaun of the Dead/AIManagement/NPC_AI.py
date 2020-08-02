import random
import math

class NPC_AI(object):
    """description of class"""
    def __init__(self):
        self.direction=""

    def get_direction(self):
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        return self.direction

    def found_Shaun(self, NPC, player):
        a=NPC.xcor() - player.xcor()
        b = NPC.ycor() - player.ycor()
        distance = math.sqrt((a **2) + (b **2))

        if distance > 24:
            self.Shaun_is_close = False
        else:
            self.Shaun_is_close = True
        
        return self.Shaun_is_close
