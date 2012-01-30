'''
Created on 08/gen/2012

@author: Christian
'''

class SteeringOutput2D(object):
    '''
    Keeps track of both linear and angular accelerations of an object in a 2D environment.
    '''


    def __init__(self, linear, angular):
        '''
        Constructor
        '''
        self.linear = linear   #2-dimensional Float Vector
        self.angular = angular #Single Float Value