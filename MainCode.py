import pygame
import math

pygame.init()
clock = pygame.time.Clock()


display_width = 500
display_height = 500
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


true = True

while true:
    clock.tick(60)
