'''
Created on 05/feb/2012

@author: Christian
'''

import pygame
from com.schism.ai4g.movement.kinematics2d import Kinematics2D
from com.schism.ai4g.util.simple_2d_object import SimpleObject2D
from com.schism.ai4g.util.vector2d import Vector2
from random import randint
from com.schism.ai4g.movement.seek import Seek
from com.schism.ai4g.movement.arrive import Arrive
from com.schism.ai4g.movement.align import Align

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
    
    SCREEN_SIZE = (600, 600)
    
    pygame.init()
    
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    main_clock = pygame.time.Clock()
    
    kin_char = Kinematics2D( Vector2(50, 50), 0, Vector2(), 0)
    char = SimpleObject2D( kin_char, colour = (255, 255, 0))
    
    kin_tar = Kinematics2D( Vector2(150, 50),45, Vector2(), 0)
    target = SimpleObject2D( kin_tar, colour = (255, 0, 0))
    
    align = Align( char.kinematics, 
                     target.kinematics, 
                     10.0,
                     20.0,
                     10,
                     100,
                     1.0 )
    
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if (e.type == pygame.MOUSEBUTTONDOWN):
                if (e.button == 1) :
                    char.kinematics.set_position( e.pos )
                    char.kinematics.set_velocity( Vector2(randint(-15, 15), randint(-15, 15)) )
                elif (e.button == 3) :
                    target.kinematics.set_position( e.pos )
                    target.kinematics.set_velocity( Vector2() )
        
        screen.fill( (127, 127, 127) )
        
        char_sprite = pygame.transform.rotate(char.sprite, char.kinematics.orientation)
        screen.blit( char_sprite, (char.kinematics.position[0] - int(char.sprite.get_width()/2), char.kinematics.position[1] - int(char.sprite.get_height()/2) ) )
        
        tar_sprite = pygame.transform.rotate(target.sprite, target.kinematics.orientation)
        screen.blit( tar_sprite, (target.kinematics.position[0] - int(target.sprite.get_width()/2), target.kinematics.position[1] - int(target.sprite.get_height()/2) ) )  
        
        seconds_passed = main_clock.tick(100) / 1000.0
        char.kinematics.update(align.get_steering(), 30.0, seconds_passed)
        
        
        checkBoundaries(char, SCREEN_SIZE)
        checkBoundaries(target, SCREEN_SIZE)
        
        pygame.display.update()