'''Sprite list module'''

import os
import turtle

#class SpriteListManager():
    #"""Prepares the list of sprite GIFs"""
    #def __init__(self):

def load_images(folder_name):
    """Prepares a list of sprite GIFs from a folder"""
    if os.path.exists(folder_name):
        filelist = os.listdir(folder_name)
        for filename in filelist:
            turtle.register_shape(folder_name + "\\" + filename)
        return filelist
    else:
        raise Exception("Error loading images from " + folder_name + " - Check path?")