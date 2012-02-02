'''
Created on 02/feb/2012

@author: Christian
'''

import pygame

class SimpleObject2D(object):
    
    def __init__(self, kin, colour = (255, 255, 255)):
        
        self.kinematics = kin
        
        sprite_surface = pygame.Surface((50, 50)).convert_alpha()
        pygame.draw.circle(sprite_surface, colour, (25, 25), 25, 3)
        pygame.draw.line(sprite_surface, colour, (25, 25), (50, 25), 3 )
        self.sprite = sprite_surface
