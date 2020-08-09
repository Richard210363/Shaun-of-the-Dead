import random
import math

class NPC_AI(object):
    """description of class"""
    def __init__(self):
        self.direction=""

    def get_direction_random(self):
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

    def set_NPC_direction(self,NPC_left_x,NPC_left_y,NPC_forward_x,NPC_forward_y,NPC):
        self.randomly = random.randint(1,10000000)
        print("Begin print - " + str(self.randomly))
        print("NPC.x_cor - " + str(NPC.x_cor))
        print("NPC.y_cor - " + str(NPC.y_cor))
        print("NPC_left_x - " + str(NPC_left_x))
        print("NPC_left_y - " + str(NPC_left_y))
        print("NPC_forward_x - " + str(NPC_forward_x))
        print("NPC_forward_y - " + str(NPC_forward_y))
        print("End print")
        if(NPC_left_x,NPC_left_y) not in NPC.walls:
            if NPC.direction == "left":
                NPC.direction = "down"
            elif NPC.direction == "right":
                NPC.direction = "up"
            elif NPC.direction == "up":
                NPC.direction = "left"
            elif NPC.direction == "down":
                NPC.direction = "right"
            return

        if (NPC_forward_x,NPC_forward_y) in NPC.walls:
            if NPC.direction == "left":
                NPC.direction = "up"
            elif NPC.direction == "right":
                NPC.direction = "down"
            elif NPC.direction == "up":
                NPC.direction = "right"
            elif NPC.direction == "down":
                NPC.direction = "left"
            return
        else:
            return

    def get_direction_searching(self, NPC):
        pass
        if NPC.direction == "left":
            #NL = "down" x is same y is 24 less than NPC.y_cor
            NPC_left_x = NPC.x_cor
            NPC_left_y = NPC.y_cor-24
            NPC_forward_x = NPC.x_cor-24
            NPC_forward_y = NPC.y_cor
            self.set_NPC_direction(NPC_left_x,NPC_left_y,NPC_forward_x,NPC_forward_y,NPC)
        elif NPC.direction == "right":
            NPC_left_x = NPC.x_cor
            NPC_left_y = NPC.y_cor+24
            NPC_forward_x = NPC.x_cor+24
            NPC_forward_y = NPC.y_cor
            self.set_NPC_direction(NPC_left_x,NPC_left_y,NPC_forward_x,NPC_forward_y,NPC)
        elif NPC.direction == "up":
            NPC_left_x = NPC.x_cor-24
            NPC_left_y = NPC.y_cor
            NPC_forward_x = NPC.x_cor
            NPC_forward_y = NPC.y_cor+24
            self.set_NPC_direction(NPC_left_x,NPC_left_y,NPC_forward_x,NPC_forward_y,NPC)
        elif NPC.direction == "down":
            NPC_left_x = NPC.x_cor+24
            NPC_left_y = NPC.y_cor
            NPC_forward_x = NPC.x_cor
            NPC_forward_y = NPC.y_cor-24
            self.set_NPC_direction(NPC_left_x,NPC_left_y,NPC_forward_x,NPC_forward_y,NPC)

        #if NPC doesn't have a wall left then turn left
        #    if NPC doesn't have a space in front then turn right
        #        else go forward

