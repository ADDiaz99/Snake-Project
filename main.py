import pygame 
import random
from settings import *

# Set the dimensions of the screen
SCREEN_WIDTH = WIDTH        #Located in settings
SCREEN_HEIGHT = HEIGHT

#Classes
class Game:
    def __init__(self):
        pass


class Snake:
    def __init__(self):
        block = pygame.image.load("resources/sprites/tile000.png").convert()
        block_x = 100
        block_y = 100


#defs
def draw_block():
    surface.fill((110, 110, 5))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

#game setup
if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    window_title = pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    running = True

    #blocks
    block = pygame.image.load("resources/sprites/tile000.png").convert()
    block_x = 100
    block_y = 100



    while running:
        #check events and then enable quitting with the X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    block_y -= 50
                elif event.key == pygame.K_DOWN: 
                    block_y += 50 
                elif event.key == pygame.K_RIGHT:
                    block_x += 50
                elif event.key == pygame.K_LEFT:
                    block_x -= 50

        #Filling the screen with a color
        surface.fill("black")

        #RENDERING
        draw_block()

        #flip to put work on screen
        pygame.display.flip()

        clock.tick(60) #Limits fps to 60

    pygame.quit()
    #s
    