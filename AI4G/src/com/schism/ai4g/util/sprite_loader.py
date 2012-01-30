'''
Created on 08/gen/2012

@author: Christian
'''

import pygame

def get_sprite( image_path, sprite_index , sprite_dim ):
    
    image = pygame.image.load(image_path).convert_alpha()
    
    image_width = image.get_width()
    image_height= image.get_height()
    
    image_cols = int( image_width / sprite_dim[0] )
    image_rows = int( image_height / sprite_dim[1] )
    
    row_index = int( sprite_index / image_cols )
    col_index = sprite_index % image_cols
    
    rect = ( col_index * sprite_dim[1], row_index * sprite_dim[0], sprite_dim[0], sprite_dim[1] )
    #print "Rect: " + str(rect)
    sprite = image.subsurface(rect)
    
    return sprite



if __name__ == "__main__":
    
    pygame.init()
    
    screen = pygame.display.set_mode( (800, 800), 0, 32 )
    
    image = get_sprite("../../../../../resources/images/test-sprites.png", 5, (80, 80))
    
    while True:
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        screen.blit(image, (0,0))
        
        pygame.display.update()