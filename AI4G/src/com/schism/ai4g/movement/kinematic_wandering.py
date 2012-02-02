'''
Created on 02/feb/2012

@author: Christian
'''
from com.schism.ai4g.movement.kinematic_steering_output2d import KinematicSteeringOutput2D
from com.schism.ai4g.util.vector2d import Vector2
import math
import random

class KinematicWandering(object):

    def __init__(self, character, max_speed, max_rotation):
        '''
        Constructor
        '''
        self.character = character
        self.max_speed = max_speed
        self.max_rotation = max_rotation
        
    def get_steering(self):
        
        steering = KinematicSteeringOutput2D()
        
        steering.rotation = (random.random() - random.random()) * self.max_rotation
        
        steering.velocity = Vector2( math.cos( math.radians(self.character.orientation) ), 
                                     - math.sin( math.radians(self.character.orientation) ) )
        steering.velocity *= self.max_speed
        
        return steering
    
    def set_character(self, char):
        self.character = char