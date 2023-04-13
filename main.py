import pygame 
import random
from settings import *

# Set the dimensions of the screen
SCREEN_WIDTH = WIDTH        #Located in settings
SCREEN_HEIGHT = HEIGHT

#game setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_title = pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
running = True

while running:
    #check events and then enable quitting with the X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Filling the screen with a color
    screen.fill("black")

    #RENDERING

    #flip to put work on screen
    pygame.display.flip()

    clock.tick(60) #Limits fps to 60

pygame.quit()

    