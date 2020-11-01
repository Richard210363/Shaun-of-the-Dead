class enemy_animation_list(object):
    """description of class"""
    def __init__(self):
        self.up = []
        self.down = []
        self.left = []
        self.right = []
        self.walking = {"Up": self.up, "Down": self.down, "Left": self.left, "Right": self.right}
        self.dying = []
        self.female = {"Walking": self.walking, "Dying": self.dying}
        self.male = {"Walking": self.walking, "Dying": self.dying}
        self.enemy_animation_dictionary = {"Female": self.female, "Male": self.male}
        self.value = 0