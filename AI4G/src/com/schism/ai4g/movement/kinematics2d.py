'''
Created on 08/gen/2012

@author: Christian
'''

import steering_output2d
import math
from com.schism.ai4g.movement.static2d import Static2D
from com.schism.ai4g.util.vector2d import Vector2


class Kinematics2D(object):
    '''
    Stores and manages information about position and motion of an object in a 2D world. 
    '''

    def __init__(self, p, o, v, r):
        '''
        Constructor
        '''
        
        self.position = p       # 2-Dimensional Float Vector
        self.orientation = o    # Single Float Value
        self.velocity = v       # 2-Dimensional Float Vector
        self.rotation = r       # Single Float Value
        
    def update(self, steering, max_speed, time_passed):
        '''
        Updates the information of the object given a SteeringOutput object (which represents
        both linear and angular acceleration) and the time passed since last update.
        '''
        
        self.position[0] += self.velocity[0] * time_passed + 0.5 * steering.linear[0] * time_passed * time_passed
        self.position[1] += self.velocity[1] * time_passed + 0.5 * steering.linear[1] * time_passed * time_passed
        
        self.orientation += self.rotation * time_passed + 0.5 * steering.angular * time_passed * time_passed
        #self.orientation = self.get_orientation()
        
        self.velocity[0] += steering.linear[0] * time_passed
        self.velocity[1] += steering.linear[1] * time_passed
        
        self.rotation += steering.angular * time_passed
    
        if self.velocity.length() > max_speed:
            self.velocity = self.velocity.normalize()
            self.velocity *= max_speed
    
    def kinematic_update(self, steering, time_passed):
        '''
        Updates the information of the object given a KinematicSteeringOutput object (which represents
        both velocity and rotation of the object) and the time passed since last update.
        '''
        
        self.velocity[0] = steering.velocity[0]
        self.velocity[1] = steering.velocity[1]
        
        self.position[0] += self.velocity[0] * time_passed
        self.position[1] += self.velocity[1] * time_passed
        
        self.rotation = steering.rotation
        
        #self.orientation = self.get_orientation()
        self.orientation += self.rotation * time_passed
    
    def get_orientation(self):
        '''
        Calculates the orientation of an object standing only on its velocity vector
        '''
        lenght = self.velocity.length()
        if (lenght > 0):
            cos_alpha = self.velocity[0] / lenght
            return -math.degrees(math.atan2(self.velocity[1], self.velocity[0]))
        return self.orientation
    
    def get_static(self):
        return Static2D( self.position, self.orientation)
    
    def set_position(self, new_pos):
        self.position[0] = new_pos[0]
        self.position[1] = new_pos[1]
        
    def set_velocity(self, new_vel):
        self.velocity[0] = new_vel[0]
        self.velocity[1] = new_vel[1]
    
    def to_string(self):
        
        return "POSITION:   X: %d   Y: %d \n\r ORIENTATION:   %.4f \n VELOCITY:   X: %d   Y: %d \n ROTATION:   %.4f" % (self.position[0], self.position[1], self.orientation, self.velocity[0], self.velocity[1], self.rotation)