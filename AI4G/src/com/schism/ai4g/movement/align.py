'''
Created on 05/feb/2012

@author: Christian
'''
from com.schism.ai4g.movement.steering_output2d import SteeringOutput2D
from com.schism.ai4g.util.vector2d import Vector2
import math

class Align(object):

    def __init__(self, char, target, max_angular_acceleration, max_rotation, target_radius, slow_radius, time_to_target ):
        '''
        Constructor
        '''
        self.character = char
        self.target = target
        self.max_angular_acceleration = max_angular_acceleration
        self.max_rotation = max_rotation
        self.target_radius = target_radius
        self.slow_radius = slow_radius
        self.time_to_target = time_to_target
    
    def map_to_range(self, rotation):
        return rotation % 360.0
        
    def get_steering(self):
        
        steering = SteeringOutput2D( Vector2(0., 0.), 0)
        
        rotation = self.target.orientation - self.character.orientation
        rotation = self.map_to_range(rotation)
        rotation_size = abs(rotation)
        
        print rotation
        
        if rotation_size < self.target_radius:
            return steering
        
        if rotation_size > self.slow_radius:
            target_speed = self.max_rotation
        else:
            target_rotation = self.max_rotation * rotation_size / self.slow_radius
            
        target_rotation *= rotation / rotation_size
        
        steering.angular = target_rotation - self.character.rotation
        steering.angular /= self.time_to_target
        
        angular_acceleration = abs(steering.angular)
        if angular_acceleration > self.max_angular_acceleration:
            steering.angular /= angular_acceleration
            steering.angular *= self.max_angular_acceleration
            
        steering.linear = 0
        
        return steering