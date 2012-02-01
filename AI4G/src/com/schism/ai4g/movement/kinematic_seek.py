'''
Created on 31/gen/2012

@author: Christian
'''
from com.schism.ai4g.movement.kinematic_steering_output2d import KinematicSteeringOutput2D

class KinematicSeek(object):

    def __init__(self, character, target, max_speed = 0.):
        '''
        Constructor
        '''
        
        #Holds only the static data of those two objects
        self.character = character
        self.target = target
        
        self.max_speed = max_speed
        
    def getSteering(self):
        
        steering = KinematicSteeringOutput2D()

        steering.velocity = self.character.position - self.target.position
        steering.velocity = steering.velocity.normalize()
        steering.velocity *= self.max_speed
        
        steering.rotation = 0
        
        return steering
         
        
        
        
    