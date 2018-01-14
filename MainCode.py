import pygame
import time
import random
import math

pygame.init()
clock = pygame.time.Clock()
#test comment

es = 40

display_width = 450 + 4*es
display_height = 450 + 4*es
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

mini_squares00 = [[True,True,True],[True,True,True],[True,True,True]]
mini_squares01 = [[True,True,True],[True,True,True],[True,True,True]]
mini_squares02 = [[True,True,True],[True,True,True],[True,True,True]]
mini_squares10 = [[True,True,True],[True,True,True],[True,True,True]]
mini_squares11 = [[True,True,True],[True,True,True],[True,True,True]]
mini_squares12 = [[True,True,True],[True,True,True],[True,True,True]]
mini_squares20 = [[True,True,True],[True,True,True],[True,True,True]]
mini_squares21 = [[True,True,True],[True,True,True],[True,True,True]]
mini_squares22 = [[True,True,True],[True,True,True],[True,True,True]]
squares = [[mini_squares00,mini_squares01,mini_squares02],[mini_squares10,mini_squares11,mini_squares12],[mini_squares20,mini_squares21,mini_squares22]]

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
        pygame.draw.rect(game_display, black, (pos_x,pos_y,width,height))
        pygame.draw.line(game_display, blue, (pos_x+5,pos_y+25), (pos_x+45,pos_y+25),5)
        pygame.draw.line(game_display, blue, (pos_x+25,pos_y+5), (pos_x+25,pos_y+45),5)
        if click[0] == 1:
            time.sleep(0.1)
            squares[X][Y][x][y] = False
    else:
        pygame.draw.rect(game_display, colour, (pos_x,pos_y,width,height))
    return squares

def check_if_gameover():
    return False

def intro_loop(intro = True, squares = squares):
    gameover = False
    Player1 = True
    width = 50
    mouse = pygame.mouse.get_pos()
    while gameover == False:
        while Player1 == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #Player 1 has turn
            game_display.fill(black)
            size = 150
            shape = ((1*size+es,1*size+es),(0+es,1*size+es),(0+es,1*size+2*es),(1*size+es,1*size+2*es),(1*size+es,2*size+2*es),(0+es,2*size+2*es), (0+es,2*size+3*es),(1*size+es,2*size+3*es),(1*size+es,3*size+3*es),(1*size+2*es,3*size+3*es),(1*size+2*es,2*size+3*es), (2*size+es,2*size+3*es),(2*size+2*es,2*size+3*es),(2*size+2*es,3*size+3*es),(2*size+3*es,3*size+3*es), (2*size+3*es,2*size+3*es),(3*size+3*es,2*size+3*es),(3*size+2*es,2*size+3*es),(3*size+3*es,2*size+3*es), (3*size+3*es,2*size+2*es),(2*size+3*es,2*size+2*es),(2*size+3*es,2*size+3*es),(2*size+3*es,1*size+2*es), (3*size+3*es,1*size+2*es),(3*size+3*es,1*size+es),(2*size+3*es,1*size+es),(2*size+3*es,0+es),(2*size+2*es,0+es), (2*size+2*es,1*size+es),(1*size+2*es,1*size+es),(1*size+2*es,0+es),(1*size+2*es,0+es),(1*size+es,0+es))
            pygame.draw.polygon(game_display, blue, shape)
            for LargeX in range(0,3):
                for LargeY in range(0,3):
                    for MiniX in range(0,3):
                        for MiniY in range(0,3):
                            pos_x = (150+es)*LargeX+50*MiniX+es
                            pos_y = (150+es)*LargeY+50*MiniY+es
                            if squares[LargeX][LargeY][MiniX][MiniY] == True:
                                squares = create_button(pos_x, pos_y, LargeX, LargeY, MiniX, MiniY, squares)
                            else:
                                pygame.draw.rect(game_display, black, (pos_x,pos_y,50,50))
                                pygame.draw.line(game_display, yellow, (pos_x+5,pos_y+5), (pos_x+45,pos_y+45),5)
                                pygame.draw.line(game_display, yellow, (pos_x+5,pos_y+45), (pos_x+45,pos_y+5),5)
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                Player1 = False
                print("Player2's Turn")

            pygame.display.update()
            clock.tick(ticker)

        while Player1 == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #Player 2 has turn
            game_display.fill(black)
            size = 150
            shape = ((1*size+es,1*size+es),(0+es,1*size+es),(0+es,1*size+2*es),(1*size+es,1*size+2*es),(1*size+es,2*size+2*es),(0+es,2*size+2*es), (0+es,2*size+3*es),(1*size+es,2*size+3*es),(1*size+es,3*size+3*es),(1*size+2*es,3*size+3*es),(1*size+2*es,2*size+3*es), (2*size+es,2*size+3*es),(2*size+2*es,2*size+3*es),(2*size+2*es,3*size+3*es),(2*size+3*es,3*size+3*es), (2*size+3*es,2*size+3*es),(3*size+3*es,2*size+3*es),(3*size+2*es,2*size+3*es),(3*size+3*es,2*size+3*es), (3*size+3*es,2*size+2*es),(2*size+3*es,2*size+2*es),(2*size+3*es,2*size+3*es),(2*size+3*es,1*size+2*es), (3*size+3*es,1*size+2*es),(3*size+3*es,1*size+es),(2*size+3*es,1*size+es),(2*size+3*es,0+es),(2*size+2*es,0+es), (2*size+2*es,1*size+es),(1*size+2*es,1*size+es),(1*size+2*es,0+es),(1*size+2*es,0+es),(1*size+es,0+es))
            pygame.draw.polygon(game_display, blue, shape)
            for LargeX in range(0,3):
                for LargeY in range(0,3):
                    for MiniX in range(0,3):
                        for MiniY in range(0,3):
                            pos_x = (150+es)*LargeX+50*MiniX+es
                            pos_y = (150+es)*LargeY+50*MiniY+es
                            if squares[LargeX][LargeY][MiniX][MiniY] == True:
                                squares = create_button(pos_x, pos_y, LargeX, LargeY, MiniX, MiniY, squares)
                            else:
                                pygame.draw.rect(game_display, black, (pos_x,pos_y,50,50))
                                pygame.draw.circle(game_display, green, (pos_x+25,pos_y+25), 23)
                                pygame.draw.circle(game_display, black, (pos_x+25,pos_y+25), 19)
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                print("Player 1's turn")
                Player1 = True

            pygame.display.update()
            clock.tick(ticker)

            gameover = check_if_gameover()

intro_loop()
