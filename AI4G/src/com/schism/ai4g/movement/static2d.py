'''
Created on 31/gen/2012

@author: Christian
'''
from com.schism.ai4g.util.vector2d import Vector2

class Static2D(object):
    '''
    Keeps track of static data of an object in a 2D environment (position and orientation).
    '''


    def __init__(self, position = Vector2(0., 0.), orientation = 0 ):
        '''
        Constructor
        '''
        self.position = position   #2-dimensional Float Vector
        self.orientation = orientation #Single Float Value