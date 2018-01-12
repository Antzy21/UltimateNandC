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

def message_display(text = '"insert text"',text_size = 20, position = (display_width/2,display_height/2), colour = white):
    largeText = pygame.font.Font('freesansbold.ttf',text_size)
    text_surface = largeText.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    game_display.blit(text_surface, text_rect)

def create_button(x , y, width, height, colour = red, hover_colour = white, text = 'hello', text_colour = black, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width/2 > mouse[0] > x - width/2 and y + height/2 > mouse[1] > y - height/2:
        pygame.draw.rect(game_display, hover_colour, (x-width/2,y-height/2,width,height))
        if click[0] == 1 and action != None:
            time.sleep(0.2)
            action()
    else:
        pygame.draw.rect(game_display, colour, (x-width/2,y-height/2,width,height))
    message_display(text = text, position = (x,y), colour = text_colour)

ticker = 10

while counter < 2*ticker:
    create_button(200,200,100,100)
    pygame.display.update()
    clock.tick(ticker)
    counter += 1
