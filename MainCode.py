import pygame
import time
import random
import math

pygame.init()
clock = pygame.time.Clock()
#test comment

es = 5

display_width = 450
display_height = 450
game_display = pygame.display.set_mode((display_width + 4*es,display_height + 4*es))
pygame.display.set_caption('Ultitmate Naughts and Crosses')

# Create colours
black  = (0,0,0)
white  = (255,255,255)
red    = (255,0,0)
green  = (0,255,0)
blue   = (0,0,255)
cyan   = (0,255,255)
yellow = (255,255,0)

ticker = 60

ms00 = [[True,True,True],[True,True,True],[True,True,True]]
ms01 = [[True,True,True],[True,True,True],[True,True,True]]
ms02 = [[True,True,True],[True,True,True],[True,True,True]]
ms10 = [[True,True,True],[True,True,True],[True,True,True]]
ms11 = [[True,True,True],[True,True,True],[True,True,True]]
ms12 = [[True,True,True],[True,True,True],[True,True,True]]
ms20 = [[True,True,True],[True,True,True],[True,True,True]]
ms21 = [[True,True,True],[True,True,True],[True,True,True]]
ms22 = [[True,True,True],[True,True,True],[True,True,True]]
squares = [[ms00,ms01,ms02],[ms10,ms11,ms12],[ms20,ms21,ms22]]

def message_display(text = '"insert text"',text_size = 20, position = (display_width/2,display_height/2), colour = white):
    largeText = pygame.font.Font('freesansbold.ttf',text_size)
    text_surface = largeText.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    game_display.blit(text_surface, text_rect)

def Crosses_button(pos_x, pos_y, X, Y, x, y, squares, Crosses, width=50, height=50, colour = white, hover_colour = white):
    if Crosses:
        Crosses = True
    else:
        Crosses == False
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos_x + width > mouse[0] > pos_x and pos_y + height > mouse[1] > pos_y:
        pygame.draw.rect(game_display, cyan, (pos_x,pos_y,width,height))
        pygame.draw.line(game_display, black, (pos_x+5,pos_y+25), (pos_x+45,pos_y+25),5)
        pygame.draw.line(game_display, black, (pos_x+25,pos_y+5), (pos_x+25,pos_y+45),5)
        if click[0] == 1:
            time.sleep(0.1)
            squares[X][Y][x][y] = 'Crosses'
            print('Crosses is now false')
            Crosses = False
    else:
        pygame.draw.rect(game_display, colour, (pos_x,pos_y,width,height))
    return squares, Crosses

def Naughts_button(pos_x, pos_y, X, Y, x, y, squares, Crosses, width=50, height=50, colour = white, hover_colour = white):
    if Crosses:
        Crosses = True
    else:
        Crosses == False
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos_x + width > mouse[0] > pos_x and pos_y + height > mouse[1] > pos_y:
        pygame.draw.rect(game_display, white, (pos_x,pos_y,width,height))
        pygame.draw.line(game_display, black, (pos_x+5,pos_y+25), (pos_x+45,pos_y+25),5)
        pygame.draw.line(game_display, black, (pos_x+25,pos_y+5), (pos_x+25,pos_y+45),5)
        if click[0] == 1:
            time.sleep(0.1)
            squares[X][Y][x][y] = 'Naughts'
            print('Crosses is now true')
            Crosses = True
    else:
        pygame.draw.rect(game_display, colour, (pos_x,pos_y,width,height))
    return squares, Crosses

def UndoNaughts(squares, Crosses, X, Y, x, y, pos_x, pos_y):
    if (pygame.key.get_pressed()[pygame.K_z]) and Crosses == True:
        mouse = pygame.mouse.get_pos()
        if pos_x + 50 > mouse[0] > pos_x and pos_y + 50 > mouse[1] > pos_y:
            click = pygame.mouse.get_pressed()
            print(click[0])
            if click[0] == 1:
                print('clicked')
                time.sleep(0.1)
                squares[X][Y][x][y] = True
                Crosses = False
    return squares, Crosses

def UndoCrosses(squares, Crosses, X, Y, x, y, pos_x, pos_y):
    if (pygame.key.get_pressed()[pygame.K_z]) and Crosses == False:
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if pos_x + 50 > mouse[0] > pos_x and pos_y + 50 > mouse[1] > pos_y:
            if click[0] == 1:
                print('clicked')
                time.sleep(0.1)
                squares[X][Y][x][y] = True
                Crosses = True
    return squares, Crosses

def check_if_gameover():
    return False

def HasMiniGameWon(squares,LargeX,LargeY):
    winner = 'no winner'
    for Type in ['Naughts', 'Crosses']:
        if squares[LargeX][LargeY][1][1] == Type: # if middle square is equal to the tpye
            if squares[LargeX][LargeY][1][0] == Type and squares[LargeX][LargeY][1][2] == Type: # if left middle and right middle
                winner = 'The winner is' + Type
            if squares[LargeX][LargeY][0][0] == Type and squares[LargeX][LargeY][2][2] == Type: # if top right and bottom left
                winner = 'The winner is' + Type
            if squares[LargeX][LargeY][0][1] == Type and squares[LargeX][LargeY][2][1] == Type: # if top middle and bottom middle
                winner = 'The winner is' + Type
            if squares[LargeX][LargeY][0][2] == Type and squares[LargeX][LargeY][2][0] == Type: # if bottom left and top right
                winner = 'The winner is' + Type
        if squares[LargeX][LargeY][0][0] == Type: # if top left has won
            if squares[LargeX][LargeY][0][1] == Type and squares[LargeX][LargeY][0][2] == Type: # if top middle and top right
                winner = 'The winner is' + Type
            if squares[LargeX][LargeY][1][0] == Type and squares[LargeX][LargeY][2][0] == Type: # if right middle and bottom right
                winner = 'The winner is' + Type
        if squares[LargeX][LargeY][2][2] == Type: # if bottom left has won
            if squares[LargeX][LargeY][0][2] == Type and squares[LargeX][LargeY][1][2] == Type: # top right and middle right
                winner = 'The winner is' + Type
            if squares[LargeX][LargeY][2][0] == Type and squares[LargeX][LargeY][2][1] == Type: # bottom left and bottom middle
                winner = 'The winner is' + Type
    return winner

def intro_loop(intro = True, squares = squares):
    gameover = False
    Crosses = True
    width = 50
    mouse = pygame.mouse.get_pos()
    undo = False

    while gameover == False:
        if Crosses == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #Crosses has turn
            game_display.fill(white)
            size = 150
            pygame.draw.rect(game_display, black, (es,es,display_width+2*es,display_height+2*es))
            for LargeX in range(0,3):
                for LargeY in range(0,3):
                    click = pygame.mouse.get_pressed()
                    #if click[0] == 1:
                        #print(HasMiniGameWon(squares,LargeX,LargeY),'for the large box (',LargeX,',',LargeY,')')
                    for MiniX in range(0,3):
                        for MiniY in range(0,3):
                            pos_x = (150+es)*LargeX+50*MiniX+es
                            pos_y = (150+es)*LargeY+50*MiniY+es
                            if squares[LargeX][LargeY][MiniX][MiniY] == True:

                                # Makes button
                                squares, Crosses = Crosses_button(pos_x, pos_y, LargeX, LargeY, MiniX, MiniY, squares, Crosses)

                            elif squares[LargeX][LargeY][MiniX][MiniY] == 'Naughts':

                                # Draws Cicle
                                pygame.draw.rect(game_display, white, (pos_x,pos_y,50,50))
                                pygame.draw.circle(game_display, blue, (pos_x+25,pos_y+25), 23)
                                pygame.draw.circle(game_display, white, (pos_x+25,pos_y+25), 19)

                                # Undo button
                                squares, Crosses = UndoNaughts(squares, Crosses, LargeX, LargeY, MiniX, MiniY, pos_x, pos_y)

                            elif squares[LargeX][LargeY][MiniX][MiniY] == 'Crosses':

                                # Draws Cross
                                pygame.draw.rect(game_display, white, (pos_x,pos_y,50,50))
                                pygame.draw.line(game_display, red, (pos_x+5,pos_y+5), (pos_x+45,pos_y+45),5)
                                pygame.draw.line(game_display, red, (pos_x+5,pos_y+45), (pos_x+45,pos_y+5),5)

                                # Undo button
                                #squares, Crosses = UndoNaughts(squares, Crosses, LargeX, LargeY, MiniX, MiniY, pos_x, pos_y)

            pygame.display.update()
            clock.tick(ticker)

        elif Crosses == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #Naughts has turn
            game_display.fill(white)
            size = 150
            shape = ((1*size+es,1*size+es),(0+es,1*size+es),(0+es,1*size+2*es),(1*size+es,1*size+2*es),(1*size+es,2*size+2*es),(0+es,2*size+2*es), (0+es,2*size+3*es),(1*size+es,2*size+3*es),(1*size+es,3*size+3*es),(1*size+2*es,3*size+3*es),(1*size+2*es,2*size+3*es), (2*size+es,2*size+3*es),(2*size+2*es,2*size+3*es),(2*size+2*es,3*size+3*es),(2*size+3*es,3*size+3*es), (2*size+3*es,2*size+3*es),(3*size+3*es,2*size+3*es),(3*size+2*es,2*size+3*es),(3*size+3*es,2*size+3*es), (3*size+3*es,2*size+2*es),(2*size+3*es,2*size+2*es),(2*size+3*es,2*size+3*es),(2*size+3*es,1*size+2*es), (3*size+3*es,1*size+2*es),(3*size+3*es,1*size+es),(2*size+3*es,1*size+es),(2*size+3*es,0+es),(2*size+2*es,0+es), (2*size+2*es,1*size+es),(1*size+2*es,1*size+es),(1*size+2*es,0+es),(1*size+2*es,0+es),(1*size+es,0+es))
            pygame.draw.polygon(game_display, black, shape)
            for LargeX in range(0,3):
                for LargeY in range(0,3):
                    for MiniX in range(0,3):
                        for MiniY in range(0,3):
                            pos_x = (150+es)*LargeX+50*MiniX+es
                            pos_y = (150+es)*LargeY+50*MiniY+es
                            if squares[LargeX][LargeY][MiniX][MiniY] == True:

                                # Make buton
                                squares, Crosses = Naughts_button(pos_x, pos_y, LargeX, LargeY, MiniX, MiniY, squares, Crosses)

                            elif squares[LargeX][LargeY][MiniX][MiniY] == 'Naughts':

                                # Make Naught
                                pygame.draw.rect(game_display, white, (pos_x,pos_y,50,50))
                                pygame.draw.circle(game_display, blue, (pos_x+25,pos_y+25), 23)
                                pygame.draw.circle(game_display, white, (pos_x+25,pos_y+25), 19)

                                # Undo button
                                #squares, Crosses = UndoCrosses(squares, Crosses, LargeX, LargeY, MiniX, MiniY, pos_x, pos_y)


                            elif squares[LargeX][LargeY][MiniX][MiniY] == 'Crosses':

                                # Make Cross
                                pygame.draw.rect(game_display, white, (pos_x,pos_y,50,50))
                                pygame.draw.line(game_display, red, (pos_x+5,pos_y+5), (pos_x+45,pos_y+45),5)
                                pygame.draw.line(game_display, red, (pos_x+5,pos_y+45), (pos_x+45,pos_y+5),5)

                                # Undo button
                                squares, Crosses = UndoCrosses(squares, Crosses, LargeX, LargeY, MiniX, MiniY, pos_x, pos_y)


            pygame.display.update()
            clock.tick(ticker)

            gameover = check_if_gameover()

intro_loop()
