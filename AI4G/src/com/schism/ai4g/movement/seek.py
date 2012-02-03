'''
Created on 03/feb/2012

@author: Christian
'''
from com.schism.ai4g.movement.steering_output2d import SteeringOutput2D
from com.schism.ai4g.util.vector2d import Vector2

class Seek(object):
    '''
    classdocs
    '''


    def __init__(self, character, target, max_acceleration):
        self.character = character
        self.target = target
        self.max_acceleration = max_acceleration
        
    def get_steering(self):
        steering = SteeringOutput2D(Vector2(0., 0.), 0)
        
        steering.linear = self.target.position - self.character.position
        
        steering.linear = steering.linear.normalize()
        steering.linear *= self.max_acceleration
        
        steering.angular = 0
        
        return steering