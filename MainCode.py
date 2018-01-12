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

mini_squares = [[True,True,True],[True,True,True],[True,True,True]]
squares = [[mini_squares,mini_squares,mini_squares],[mini_squares,mini_squares,mini_squares],[mini_squares,mini_squares,[[True,True,True],[True,True,True],[True,True,True]]]]

def message_display(text = '"insert text"',text_size = 20, position = (display_width/2,display_height/2), colour = white):
    largeText = pygame.font.Font('freesansbold.ttf',text_size)
    text_surface = largeText.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    game_display.blit(text_surface, text_rect)

def create_button(pos_x, pos_y, X, Y, x, y, squares, width=50, height=50, colour = red, hover_colour = white):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos_x + width > mouse[0] > pos_x and pos_y + height > mouse[1] > pos_y:
        pygame.draw.rect(game_display, hover_colour, (pos_x,pos_y,width,height))
        pygame.draw.line(game_display, blue, (pos_x+5,pos_y+5), (pos_x+45,pos_y+45),5)
        pygame.draw.line(game_display, blue, (pos_x+5,pos_y+45), (pos_x+45,pos_y+5),5)
        if click[0] == 1:
            time.sleep(0.2)
            squares[X][Y][x][y] = False
    else:
        pygame.draw.rect(game_display, colour, (pos_x,pos_y,width,height))
    return squares

def check_if_gameover():
    return False

def intro_loop(intro = True, squares = squares):
    gameover = False
    Player1 = True
    while gameover == False:
        if Player1 == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #Player 1 has turn
            game_display.fill(black)
            for LargeX in range(0,3):
                for LargeY in range(0,3):
                    #pygame.draw.polygon(game_display, green, ((25,75),(76,125),(250,375),(400,25),(60,540)))
                    for MiniX in range(0,3):
                        for MiniY in range(0,3):
                            print(squares[LargeX][LargeY][MiniX][MiniY])
                            x = 2*edgespace + (150+2*edgespace)*LargeX+50*MiniX
                            y = 2*edgespace + (150+2*edgespace)*LargeY+50*MiniY
                            if squares[LargeX][LargeY][MiniX][MiniY] == True:
                                squares = create_button(x, y, LargeX, LargeY, MiniX, MiniY, squares)
                            else:
                                pygame.draw.rect(game_display, blue, (x,y,10,10))

            pygame.display.update()
            clock.tick(ticker)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #Player 2 has turn
            game_display.fill(black)
            for LargeX in range(0,3):
                for LargeY in range(0,3):
                    #pygame.draw.polygon(game_display, green, ((25,75),(76,125),(250,375),(400,25),(60,540)))
                    for MiniX in range(0,3):
                        for MiniY in range(0,3):
                            x = 2*edgespace + (150+2*edgespace)*LargeX+50*MiniX
                            y = 2*edgespace + (150+2*edgespace)*LargeY+50*MiniY
                            if squares[LargeX][LargeY][MiniX][MiniY] == True:
                                create_button(x,y)
                            else:
                                pygame.draw.rect(game_display, blue, (x,y,10,10))


            pygame.display.update()
            clock.tick(ticker)

        gameover = check_if_gameover()

intro_loop()
