'''
Created on 05/feb/2012

@author: Christian
'''
from com.schism.ai4g.movement import steering_output2d
from com.schism.ai4g.movement.steering_output2d import SteeringOutput2D
from com.schism.ai4g.util.vector2d import Vector2

class Arrive(object):

    def __init__(self, char, target, max_acceleration, max_speed, target_radius, slow_radius, time_to_target ):
        '''
        Constructor
        '''
        self.character = char
        self.target = target
        self.max_acceleration = max_acceleration
        self.max_speed = max_speed
        self.target_radius = target_radius
        self.slow_radius = slow_radius
        self.time_to_target = time_to_target
        
    def get_steering(self):
        
        steering = SteeringOutput2D( Vector2(0., 0.), 0)
        
        direction = self.target.position - self.character.position
        distance = direction.length()
        
        if distance < self.target_radius:
            return steering
        
        if distance > self.slow_radius:
            target_speed = self.max_speed
        else:
            target_speed = self.max_speed * distance / self.slow_radius
            
        target_velocity = direction
        target_velocity = target_velocity.normalize()
        target_velocity *= target_speed
        
        steering.linear = target_velocity - self.character.velocity
        steering.linear /= self.time_to_target
        
        if steering.linear.length() > self.max_acceleration:
            steering.linear = steering.linear.normalize()
            steering.linear *= self.max_acceleration
            
        steering.angular = 0
        
        return steering
        
        