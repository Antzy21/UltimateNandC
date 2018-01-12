import pygame
import time
import random
import math

pygame.init()
clock = pygame.time.Clock()
#test comment

edgespace = 2

display_width = 450 + 8*edgespace
display_height = 450 + 8*edgespace
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

ticker = 120

def message_display(text = '"insert text"',text_size = 20, position = (display_width/2,display_height/2), colour = white):
    largeText = pygame.font.Font('freesansbold.ttf',text_size)
    text_surface = largeText.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    game_display.blit(text_surface, text_rect)

def create_button(x , y, width=50, height=50, colour = red, hover_colour = white, text = 'hello', text_colour = black, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(game_display, hover_colour, (x,y,width,height))
        if click[0] == 1 and action != None:
            time.sleep(0.2)
            action()

    else:
        pygame.draw.rect(game_display, colour, (x,y,width,height))
    message_display(text = text, position = (x+width/2,y+height/2), colour = text_colour)

def intro_loop(intro = True):
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(black)
        for LargeX in range(0,3):
            for LargeY in range(0,3):
                for MiniX in range(0,3):
                    for MiniY in range(0,3):
                        x = 2*edgespace + (150+2*edgespace)*LargeX+50*MiniX
                        y = 2*edgespace + (150+2*edgespace)*LargeY+50*MiniY
                        create_button(x,y)



        pygame.display.update()
        clock.tick(ticker)

intro_loop()
