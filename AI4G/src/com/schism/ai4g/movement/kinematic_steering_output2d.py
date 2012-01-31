'''
Created on 31/gen/2012

@author: Christian
'''
from com.schism.ai4g.util.vector2d import Vector2

class KinematicSteeringOutput2D(object):

    def __init__(self, velocity = Vector2(0., 0.), rotation = 0):
        '''
        Constructor
        '''
        self.velocity = velocity   #2-dimensional Float Vector
        self.rotation = rotation   #Single Float Value