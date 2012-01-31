'''
Created on 31/gen/2012

@author: Christian
'''

import math

class Vector2(object):
    '''
    Class that implements a 2-dimensional float vector
    '''


    def __init__(self, x = 0, y = 0):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        
    def __getitem__(self, key):
        if( key == 0):
            return self.x
        elif( key == 1):
            return self.y
        else:
            raise Exception("Invalid key to Point")
        
    def __setitem__(self, key, value):
        if( key == 0):
            self.x = value
        elif( key == 1):
            self.y = value
        else:
            raise Exception("Invalid key to Point")        
        
    def __add__(self, v):
        return Vector2( self[0] + v[0], self[1] + v[1] )
        
    def __iadd__(self, v):
        self[0] = self[0] + v[0]
        self[1] = self[1] + v[1]
        return self
    
    def __sub__(self, v):
        return Vector2( self[0] - v[0], self[1] - v[1] )
        
    def __isub__(self, v):
        self[0] = self[0] - v[0]
        self[1] = self[1] - v[1]
        return self
    
    def __mul__(self, val):
        return Vector2( self[0] * val, self[1] * val )
    
    def __imul__(self, val):
        self[0] = self[0] * val
        self[1] = self[1] * val
        return self
    
    def __div__(self, val):
        return Vector2( self[0] / val, self[1] / val )
    
    def __idiv__(self, val):
        self[0] = self[0] / val
        self[1] = self[1] / val
        return self
        
    def length(self):
        return math.sqrt( self[0]**2 + self[1]**2 )
    
    def normalize( self ):
        if( self[0] == 0. and self[1] == 0. ):
            return Vector2(0., 0.)
        return self / self.length()
    
    