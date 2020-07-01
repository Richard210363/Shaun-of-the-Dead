class SoundEffects(object):
    """Set up variables to contain sounds"""

import pygame

#prepare sound
pygame.mixer.init()

bulletSound = pygame.mixer.Sound('..\Resources\Sounds\laser1.wav')