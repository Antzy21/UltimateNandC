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
    width = 50
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    while gameover == False:
        while Player1 == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #Player 1 has turn
            game_display.fill(black)
            for LargeX in range(0,3):
                for LargeY in range(0,3):
<<<<<<< HEAD
                    print("test")
                    shape = ((50,50),(0,50),(0,50+es),(50,50+es),(50,100+es),(0,100+es),(0,100+2*es),(50,100+2*es),(50,150+2*es),(50+es,150+2*es),(50+es,100+2*es),(100,100+2*es),(100+es,100+2*es),(100+es,150+2*es),(100+2*es,150+2*es),(100+2*es,100+2*es),(150+2*es,100+2*es),(150+es,100+2*es),(150+2*es,100+2*es),(150+2*es,100+es),(100+2*es,100+es),(100+2*es,100+2*es),(100+2*es,50+2*es),(150+2*es,50+2*es),(150+2*es,50+es),(100+2*es,50+es),(100+2*es,0+2*es),(100+es,0+2*es),(100+es,50+2*es))
=======
                    shape = ((150,150),(0,150),(0,150+es),(150,150+es),(150,300+es),(0,300+es), (0,300+2*es),(150,300+2*es),(150,450+2*es),(150+es,450+2*es),(150+es,300+2*es), (300,300+2*es),(300+es,300+2*es),(300+es,450+2*es),(300+2*es,450+2*es), (300+2*es,300+2*es),(450+2*es,300+2*es),(450+es,300+2*es),(450+2*es,300+2*es), (450+2*es,300+es),(300+2*es,300+es),(300+2*es,300+2*es),(300+2*es,150+es), (450+2*es,150+es),(450+2*es,150),(300+2*es,150),(300+2*es,0),(300+es,0), (300+es,150),(150+es,150),(150+es,0),(150+es,0),(150,0))
>>>>>>> 6e90c4c8385c74e816e1107ef4ab14daeb3b0d6d
                    pygame.draw.polygon(game_display, blue, shape)
                    for MiniX in range(0,3):
                        for MiniY in range(0,3):
                            pos_x = (150+es)*LargeX+50*MiniX
                            pos_y = (150+es)*LargeY+50*MiniY
                            if squares[LargeX][LargeY][MiniX][MiniY] == True:
                                squares = create_button(pos_x, pos_y, LargeX, LargeY, MiniX, MiniY, squares)
                            else:
                                pygame.draw.rect(game_display, blue, (pos_x,pos_y,10,10))
<<<<<<< HEAD
                            if click[0] == 1:
                                Player1 == False
=======
            click = pygame.mouse.get_pressed()
            if click[0] == 1 and [[click[0]],[pos_x + width > mouse[0] > pos_x and pos_y + height > mouse[1] > pos_y]]:
                Player1 == False
>>>>>>> 6e90c4c8385c74e816e1107ef4ab14daeb3b0d6d

            pygame.display.update()
            clock.tick(ticker)
        while Player1 == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #Player 2 has turn
            game_display.fill(cyan)
            time.sleep(2)
            for LargeX in range(0,3):
                for LargeY in range(0,3):
                    #pygame.draw.polygon(game_display, green, ((25,75),(76,125),(250,375),(400,25),(60,540)))
                    for MiniX in range(0,3):
                        for MiniY in range(0,3):
                            x = 2*es + (150+2*es)*LargeX+50*MiniX
                            y = 2*es + (150+2*es)*LargeY+50*MiniY
                            if squares[LargeX][LargeY][MiniX][MiniY] == True:
                                squares = create_button(x, y, LargeX, LargeY, MiniX, MiniY, squares)
                            else:
                                pygame.draw.rect(game_display, blue, (x,y,10,10))
                            if click[0] == 1:
                                Player1 == True
                                print("test2")

            pygame.display.update()
            clock.tick(ticker)

    gameover = check_if_gameover()

intro_loop()
