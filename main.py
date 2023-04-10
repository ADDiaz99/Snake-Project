import pygame 
import random
from settings import *

# Set the dimensions of the screen
SCREEN_WIDTH = WIDTH
SCREEN_HEIGHT = HEIGHT

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#################################################################  Start everything and settings
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0
score = 0


    