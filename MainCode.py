import pygame
import math

pygame.init()
clock = pygame.time.Clock()
#test comment

display_width = 450
display_height = 450
game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Ulitmate Naughts and Crosses')

# Create colours
black  = (0,0,0)
white  = (255,255,255)
red    = (255,0,0)
green  = (0,255,0)
blue   = (0,0,255)
cyan   = (0,255,255)
yellow = (255,255,0)

counter = 0

while counter < 20:
    
    clock.tick(10)
    counter += 1
