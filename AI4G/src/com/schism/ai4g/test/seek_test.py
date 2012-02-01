'''
Created on 31/gen/2012

@author: Christian
'''

import pygame
from com.schism.ai4g.movement.kinematics2d import Kinematics2D
from com.schism.ai4g.util.vector2d import Vector2
from random import randint
from com.schism.ai4g.movement.steering_output2d import SteeringOutput2D

class SimpleObject2D(object):
    
    def __init__(self, kin, colour = (255, 255, 255)):
        
        self.kinematics = kin
        
        sprite_surface = pygame.Surface((50, 50)).convert_alpha()
        pygame.draw.rect(sprite_surface, colour, (0, 0, 50, 50), 5)
        pygame.draw.line(sprite_surface, colour, (25, 25), (50, 25), 3 )
        self.sprite = sprite_surface



pygame.init()
SCREEN_SIZE = (700,700)
    
#Clock for framerate
main_clock = pygame.time.Clock()
screen = pygame.display.set_mode( SCREEN_SIZE, 0 , 32 )
font = pygame.font.SysFont("arial", 14)

def checkBoundaries( obj, SCREEN_SIZE = (100, 100) ):
    if obj.kinematics.position[0] < 0:
            obj.kinematics.position[0] = SCREEN_SIZE[0]
    elif obj.kinematics.position[0] > SCREEN_SIZE[0]:
        obj.kinematics.position[0] = 0
        
    if ( (obj.kinematics.position[1] + obj.sprite.get_height()) < 0 ):
        obj.kinematics.position[1] = SCREEN_SIZE[1]
    elif obj.kinematics.position[1] > SCREEN_SIZE[1]:
        obj.kinematics.position[1] = 0     
        
if __name__ == "__main__":
    
    #World objects
    kin_char = Kinematics2D( Vector2(), 0, Vector2(), 0)
    char = SimpleObject2D( kin_char, colour = (255, 255, 0))
    
    tar_char = Kinematics2D( Vector2(), 0, Vector2(), 0)
    target = SimpleObject2D( tar_char, colour = (255, 0, 0))
    
    steering = SteeringOutput2D( Vector2(0, 0), 3)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1) :
                    print "*** LEFT PRESSED ***"
                    char.kinematics.set_position( event.pos )
                    char.kinematics.set_velocity( Vector2(randint(1, 15), randint(1, 15)) )
                elif (event.button == 3) :
                    print "*** RIGHT PRESSED ***"
                    target.kinematics.set_position( event.pos )
                    target.kinematics.set_velocity( Vector2() )
                    #===========================================================
                    # print "Char position: ({0}, {1})".format(char.kinematics.position[0], char.kinematics.position[1])
                    # print "Target position: ({0}, {1})".format(target.kinematics.position[0], target.kinematics.position[1])
                    # print "---------------------------"
                    #===========================================================
                
        screen.fill((127,127,127))
        
        screen.blit( char.sprite, (char.kinematics.position[0], char.kinematics.position[1]) )
        screen.blit( target.sprite, (target.kinematics.position[0], target.kinematics.position[1]) )
        
        seconds_passed = main_clock.tick(100) / 1000.0
        
        char.kinematics.update(steering, seconds_passed)
        target.kinematics.update(steering, seconds_passed)
        
        checkBoundaries(char, SCREEN_SIZE)
        checkBoundaries(target, SCREEN_SIZE)
        
        pygame.display.update()
        
        