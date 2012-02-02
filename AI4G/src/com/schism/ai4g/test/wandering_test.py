'''
Created on 02/feb/2012

@author: Christian
'''

import pygame
from com.schism.ai4g.util.simple_2d_object import SimpleObject2D
from com.schism.ai4g.movement.kinematics2d import Kinematics2D
from com.schism.ai4g.util.vector2d import Vector2
from com.schism.ai4g.movement.kinematic_wandering import KinematicWandering

def checkBoundaries( obj, SCREEN_SIZE = (100, 100) ):
    if obj.kinematics.position[0] < 0:
            obj.kinematics.position[0] = SCREEN_SIZE[0]
    elif obj.kinematics.position[0] > SCREEN_SIZE[0]:
        obj.kinematics.position[0] = 0
        
    if ( (obj.kinematics.position[1] + obj.sprite.get_height()) < 0 ):
        obj.kinematics.position[1] = SCREEN_SIZE[1]
    elif obj.kinematics.position[1] > SCREEN_SIZE[1]:
        obj.kinematics.position[1] = 0   

def print_GUI(screen_surface, offset, font, obj):
    
    font_height = font.get_height()
    attributes = [ ["X Position", int(obj.kinematics.position[0])],
                   ["Y Position", int(obj.kinematics.position[1])],
                   ["Orientation", obj.kinematics.orientation],
                   ["X Velocity", obj.kinematics.velocity[0]],
                   ["Y Velocity", obj.kinematics.velocity[1]],
                   ["Rotation", obj.kinematics.rotation]]
    
    surfaces = []
    
    for (label, data) in attributes:
        surfaces.append(font.render( label + ": " + str(data) , True, (255,255,255), (127,127,127)))
    
    for surface in surfaces:   
        screen_surface.blit( surface, offset )
        offset[1] += font_height + 2

if __name__ == "__main__":
    
    SCREEN_SIZE = (600, 600)
    
    pygame.init()
    
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    font = pygame.font.SysFont("arial", 14)
    
    kin_char = Kinematics2D( Vector2(300, 300), 30, Vector2(0., 0.), 0)
    char = SimpleObject2D(kin_char, (127,127,127))
    
    wandering = KinematicWandering( char.kinematics.get_static(), 100, 200)
    
    main_clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        screen.fill((0,0,0))
        
        char_sprite = pygame.transform.rotate(char.sprite, char.kinematics.orientation)
        screen.blit( char_sprite, (char.kinematics.position[0] - int(char.sprite.get_width()/2), 
                                   char.kinematics.position[1] - int(char.sprite.get_height()/2) ))
        
        print_GUI(screen, [10, 10], font, char)
        
        seconds_passed = main_clock.tick(60) / 1000.0
        wandering.set_character(char.kinematics.get_static())
        char.kinematics.kinematic_update( wandering.get_steering(), seconds_passed)
        
        checkBoundaries(char, SCREEN_SIZE)
        
        pygame.display.update()
        
        
        