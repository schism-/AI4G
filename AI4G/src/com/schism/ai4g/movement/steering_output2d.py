'''
Created on 08/gen/2012

@author: Christian
'''
from com.schism.ai4g.util.vector2d import Vector2

class SteeringOutput2D(object):
    '''
    Keeps track of both linear and angular accelerations of an object in a 2D environment.
    '''


    def __init__(self, linear = Vector2(0., 0.), angular = 0):
        '''
        Constructor
        '''
        self.linear = linear   #2-dimensional Float Vector
        self.angular = angular #Single Float Value