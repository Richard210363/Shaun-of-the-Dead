import random

class NPC_AI(object):
    """description of class"""
    def __init__(self):
        self.direction=""

    def get_direction(self):
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        return self.direction