'''
Created on 31/gen/2012

@author: Christian
'''
from com.schism.ai4g.movement.kinematic_steering_output2d import KinematicSteeringOutput2D

class KinematicSeek(object):

    def __init__(self, character, target, max_speed = 0., radius = 0):
        '''
        Constructor
        '''
        
        #Holds only the static data of those two objects
        self.character = character
        self.target = target
        
        self.max_speed = max_speed
        self.radius = radius
        self.time_to_target = 1.2
        
        
    def get_steering(self):
        
        steering = KinematicSteeringOutput2D()
        
        steering.velocity = self.target.position - self.character.position
        
        if steering.velocity.length() < self.radius:
            steering.velocity[0] = 0.
            steering.velocity[1] = 0.
            steering.rotation = 0.
            return steering
        
        steering.velocity /= self.time_to_target
        
        if steering.velocity.length() > self.max_speed:
            steering.velocity = steering.velocity.normalize()
            steering.velocity *= self.max_speed
        
        steering.rotation = 0
        
        return steering
         
    def set_target(self, target):    
        self.target = target
        
    