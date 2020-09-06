# Basically this works out what is the "error" between the actual coordinate values on a line and which integer value is closest and then picks closest integer
#It moves in the +ve or -ve x direction and determines which y coordinate to use
#However, this uses integer maths to derive the points on a line that are integer numbers because using fractional numbers (in Python Doubles or Floats) is processor intensive.

#If you want to see how to derive the formula and the Decision Variable, see https://www.youtube.com/watch?v=RGB-wlatStc NOTE: This example for m <1
#If you just watch from 37:50 you will see how the below works

#This is the code I adapted http://floppsie.comp.glam.ac.uk/Southwales/gaius/gametools/6.html#2.%20Bresenham's%20line%20algorithm


class Bresenham(object):
    def __init__ (self, p0, p1):
        self.initial = True #first run flag
        self.end = False    #end of sequence detected flag 
        self.p0 = p0    #start coordinates
        self.p1 = p1    #end coordinates    
        self.x0 = p0[0] #start x coordinate  Also used as current the x cordinate when progressing through the algorithm
        self.y0 = p0[1] #start y coordinate  Also used as current the y cordinate when progressing through the algorithm
        self.x1 = p1[0] #end x coordinate
        self.y1 = p1[1] #end y coordinate
        self.dx = abs(self.x1-self.x0) #absolute change in x between start and end
        self.dy = abs(self.y1-self.y0) #absolute change in y between start and end

        if self.x0 < self.x1: #
            self.sx = 1     #slope in x is positive.  NOTE: This sets the integer will use to change the x coordinate
        else:
            self.sx = -1    #slope in x is negitive

        if self.y0 < self.y1:
            self.sy = 1     #slope in y is positive NOTE: This sets the integer will use to change the y coordinate
        else:
            self.sy = -1    #slope in y is negitive

        self.err = self.dx-self.dy  #The Incremental Error or Decision Variable.  It's this variable that determines which coordinate we pick next.

    def get_next (self):
        if self.initial:    #return start coordinates if this is the first time we ran this method
            self.initial = False
            return [self.x0, self.y0]

        if self.x0 == self.x1 and self.y0 == self.y1:     #return end coordinates if the current coordinates equals the end coordinates
            self.end = True
            return [self.x1, self.y1]

        self.e2 = 2*self.err
        print("e2=" + str(self.e2))# from this line to the Return is the core of the Bresenham calculation
        if self.e2 > -self.dy:
            self.err = self.err - self.dy   #We change the Incremental Error here for the next pass through the algorithm
            self.x0 = self.x0 + self.sx
        if self.e2 < self.dx:
            self.err = self.err + self.dx
            self.y0 = self.y0 + self.sy
        return [self.x0, self.y0]

    #def get_current_pos (self):
    #    return [self.x0, self.y0]

    def finished (self):
        return self.end