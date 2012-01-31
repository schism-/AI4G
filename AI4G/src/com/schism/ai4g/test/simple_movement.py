'''
Created on 08/gen/2012

@author: Christian
'''

import pygame
import com.schism.ai4g.util.sprite_loader as sprite_loader
from com.schism.ai4g.movement.kinematics2d import Kinematics2D
from random import randint
from com.schism.ai4g.movement.steering_output2d import SteeringOutput2D
from com.schism.ai4g.util.vector2d import Vector2

class SimpleObject2D(object):
    
    def __init__(self, kin, sprite_no):
        
        self.kinematics = kin
        #self.sprite = sprite_loader.get_sprite("../../../../../resources/images/test-sprites.png", sprite_no, (80, 80))
        
        sprite_surface = pygame.Surface((50, 50)).convert_alpha()
        pygame.draw.rect(sprite_surface, (255, 255, 255), (0, 0, 50, 50), 5)
        pygame.draw.line(sprite_surface, (255, 0, 0), (25, 25), (50, 25), 3 )
        self.sprite = sprite_surface
      
def print_GUI(screen_surface, offset, font, obj, steering):
    
    font_height = font.get_height()
    attributes = [ ["X Position", int(obj.kinematics.position[0])],
                   ["Y Position", int(obj.kinematics.position[1])],
                   ["Orientation", obj.kinematics.orientation],
                   ["X Velocity", obj.kinematics.velocity[0]],
                   ["Y Velocity", obj.kinematics.velocity[1]],
                   ["Rotation", obj.kinematics.rotation],
                   ["X acceleration", steering.linear[0]],
                   ["Y acceleration", steering.linear[1]],
                   ["Angular acceleration", steering.angular]]
    
    surfaces = []
    
    for (label, data) in attributes:
        surfaces.append(font.render( label + ": " + str(data) , True, (255,255,255), (127,127,127)))
    
    for surface in surfaces:   
        screen_surface.blit( surface, offset )
        offset[1] += font_height + 2

if __name__ == "__main__":
    
    pygame.init()
    
    SCREEN_SIZE = (700,700)
    
    #Clock for framerate
    main_clock = pygame.time.Clock()
    screen = pygame.display.set_mode( SCREEN_SIZE, 0 , 32 )
    font = pygame.font.SysFont("arial", 14)
    
    initial_position = Vector2( randint(1, 300), randint(1, 300) )
    initial_orientation = 0
    initial_velocity = Vector2( 0, 0 )
    initial_rotation = 0
    
    steering = SteeringOutput2D( Vector2(0, 0), 3)
    kin = Kinematics2D(initial_position, initial_orientation, initial_velocity, initial_rotation)
    
    obj = SimpleObject2D(kin, 5)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) :
                obj.kinematics.set_position( event.pos )
                obj.kinematics.set_velocity( Vector2(randint(1, 15), randint(1, 15)) )
                
        screen.fill((127,127,127))
        
        new_sprite = pygame.transform.rotate(obj.sprite, obj.kinematics.orientation % 360.0)
        screen.blit( new_sprite, (obj.kinematics.position[0], obj.kinematics.position[1]) )
        
        print_GUI(screen, [10, 10], font, obj, steering)
        
        seconds_passed = main_clock.tick(100) / 1000.0
        obj.kinematics.update(steering, seconds_passed)
        
        if obj.kinematics.position[0] < 0:
            obj.kinematics.position[0] = SCREEN_SIZE[0]
        elif obj.kinematics.position[0] > SCREEN_SIZE[0]:
            obj.kinematics.position[0] = 0
        
        if ( (obj.kinematics.position[1] + obj.sprite.get_height()) < 0 ):
            obj.kinematics.position[1] = SCREEN_SIZE[1]
        elif obj.kinematics.position[1] > SCREEN_SIZE[1]:
            obj.kinematics.position[1] = 0
        
        pygame.display.update()
        
        
        