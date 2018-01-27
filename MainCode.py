import pygame
import time
import random
import math

pygame.init()
clock = pygame.time.Clock()
#test comment

es = 5  # es = "edge space"

display_width = 450
display_height = 450
game_display = pygame.display.set_mode((display_width + 4*es,display_height + 4*es))
pygame.display.set_caption('Ultimate Naughts and Crosses')

# Create colours
black  = (0,0,0)
white  = (255,255,255)
grey   = (220,220,220)
red    = (255,0,0)
green  = (0,255,0)
blue   = (0,0,255)
blue1  = (182,255,255)
blue2  = (0,152,202)
cyan   = (0,255,255)
yellow = (255,255,0)
pink   = (242,0,133)
pink1  = (255,226,235)

ticker = 20

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

def normal_button(pos_x, pos_y, width, height, action = None, colour = cyan, hover_colour = blue2):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos_x + width > mouse[0] > pos_x and pos_y + height > mouse[1] > pos_y:
        pygame.draw.rect(game_display, hover_colour, (pos_x,pos_y,width,height))
        if click[0] == 1:
            action()
    else:
        pygame.draw.rect(game_display, colour, (pos_x,pos_y,width,height))

def Crosses_button(pos_x, pos_y, X, Y, x, y, squares, Crosses, Game_records, width=50, height=50, colour = white, hover_colour = white):
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
            Game_records.append([X,Y,x,y])
            print(Game_records[-1])
            Crosses = False
    else:
        pygame.draw.rect(game_display, colour, (pos_x,pos_y,width,height))
    return squares, Crosses, Game_records

def Naughts_button(pos_x, pos_y, X, Y, x, y, squares, Crosses, Game_records, width=50, height=50, colour = white, hover_colour = white):
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
            squares[X][Y][x][y] = 'Naughts'
            Crosses = True
            Game_records.append([X,Y,x,y])
            print(Game_records[-1])
    else:
        pygame.draw.rect(game_display, colour, (pos_x,pos_y,width,height))
    return squares, Game_records

def Undo(squares, Game_records, X, Y, x, y, pos_x, pos_y):
    if (pygame.key.get_pressed()[pygame.K_z]):
        squares[X][Y][x][y] = True
        Game_records.pop(-1)
        time.sleep(0.5)
    return squares, Game_records

def check_if_gameover(NandC):
    winner = None
    for Type in ['Naughts', 'Crosses']:
        if NandC[1][1] == Type: # if middle square is equal to the tpye
            if NandC[1][0] == Type and NandC[1][2] == Type: # if left middle and right middle
                winner = Type
            if NandC[0][0] == Type and NandC[2][2] == Type: # if top right and bottom left
                winner = Type
            if NandC[0][1] == Type and NandC[2][1] == Type: # if top middle and bottom middle
                winner = Type
            if NandC[0][2] == Type and NandC[2][0] == Type: # if bottom left and top right
                winner = Type
        if NandC[0][0] == Type: # if top left has won
            if NandC[0][1] == Type and NandC[0][2] == Type: # if top middle and top right
                winner = Type
            if NandC[1][0] == Type and NandC[2][0] == Type: # if right middle and bottom right
                winner = Type
        if NandC[2][2] == Type: # if bottom left has won
            if NandC[0][2] == Type and NandC[1][2] == Type: # top right and middle right
                winner = Type
            if NandC[2][0] == Type and NandC[2][1] == Type: # bottom left and bottom middle
                winner = Type
    return winner

def HasMiniGameWon(squares,X,Y,NandC):
    for Type in ['Naughts', 'Crosses']:
        if squares[X][Y][1][1] == Type: # if middle square is equal to the tpye
            if squares[X][Y][1][0] == Type and squares[X][Y][1][2] == Type: # if left middle and right middle
                NandC[X][Y] = Type
            if squares[X][Y][0][0] == Type and squares[X][Y][2][2] == Type: # if top right and bottom left
                NandC[X][Y] = Type
            if squares[X][Y][0][1] == Type and squares[X][Y][2][1] == Type: # if top middle and bottom middle
                NandC[X][Y] = Type
            if squares[X][Y][0][2] == Type and squares[X][Y][2][0] == Type: # if bottom left and top right
                NandC[X][Y] = Type
        if squares[X][Y][0][0] == Type: # if top left has won
            if squares[X][Y][0][1] == Type and squares[X][Y][0][2] == Type: # if top middle and top right
                NandC[X][Y] = Type
            if squares[X][Y][1][0] == Type and squares[X][Y][2][0] == Type: # if right middle and bottom right
                NandC[X][Y] = Type
        if squares[X][Y][2][2] == Type: # if bottom left has won
            if squares[X][Y][0][2] == Type and squares[X][Y][1][2] == Type: # top right and middle right
                NandC[X][Y] = Type
            if squares[X][Y][2][0] == Type and squares[X][Y][2][1] == Type: # bottom left and bottom middle
                NandC[X][Y] = Type
    return NandC

def mainmenu_loop(mainmenu = True):
    while mainmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(black)
        message_display(text = 'ULTIMATE', position = (display_width*(10/20),display_height*(4/20)), text_size = 50)
        message_display(text = 'Naughts and Crosses', position = (display_width*(10/20),display_height*(4/20)), text_size = 50)
        normal_button(50, 50, 50, 50, game_loop)

        pygame.display.update()
        clock.tick(60)
    intro = False


def game_loop(squares = squares):
    gameover = False
    Crosses = True
    width = 50
    mouse = pygame.mouse.get_pos()
    undo = False
    winner = None

    NandC = [['-','-','-'],['-','-','-'],['-','-','-']]

    Game_records = [[1,1,1,1]]

    while winner == None:
        # If Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(Game_records)
                pygame.quit()
                quit()

        #Crosses has turn
        game_display.fill(white)
        pygame.draw.rect(game_display, black, (es,es,display_width+2*es,display_height+2*es))
        for LX in range(0,3):
            for LY in range(0,3):
                for MX in range(0,3):
                    for MY in range(0,3):
                        pos_x = (150+es)*LX+50*MX+es
                        pos_y = (150+es)*LY+50*MY+es
                        if squares[LX][LY][MX][MY] == True:
                            try:
                                BigX, BigY = Game_records[-1][2:]
                                if LX == BigX and LY == BigY:
                                    if Crosses == True:
                                    # Makes Crosses button
                                        squares, Crosses, Game_records = Crosses_button(pos_x, pos_y, LX, LY, MX, MY, squares, Crosses, Game_records)
                                    elif Crosses == False:
                                    # Makes Naughts buton
                                        squares, Crosses, Game_records = Naughts_button(pos_x, pos_y, LX, LY, MX, MY, squares, Crosses, Game_records)
                                else:
                                    pygame.draw.rect(game_display, white, (pos_x,pos_y,50,50))
                            except:
                                squares, Crosses, Game_records = Crosses_button(pos_x, pos_y, LX, LY, MX, MY, squares, Crosses, Game_records)
                        elif squares[LX][LY][MX][MY] == 'Naughts':

                            # Draws Cicle
                            pygame.draw.rect(game_display, white, (pos_x,pos_y,50,50))
                            pygame.draw.circle(game_display, blue, (pos_x+25,pos_y+25), 23, 4)
                            if [LX,LY,MX,MY] == Game_records[-1]:
                                pygame.draw.rect(game_display, blue1, (pos_x,pos_y,50,50))
                                pygame.draw.circle(game_display, blue, (pos_x+25,pos_y+25), 23, 4)

                            if Crosses:
                                # Only Undo button if it is a naught (because it's crosses turn, so last thing placed was a naught)
                                squares, Crosses = UndoNaughts(squares, Crosses, LX, LY, MX, MY, pos_x, pos_y)

                        elif squares[LX][LY][MX][MY] == 'Crosses':

                            # Draws Cross
                            pygame.draw.rect(game_display, white, (pos_x,pos_y,50,50))
                            pygame.draw.line(game_display, red, (pos_x+5,pos_y+5), (pos_x+45,pos_y+45),5)
                            pygame.draw.line(game_display, red, (pos_x+5,pos_y+45), (pos_x+45,pos_y+5),5)
                            if [LX,LY,MX,MY] == Game_records[-1]:
                                pygame.draw.rect(game_display, pink1, (pos_x,pos_y,50,50))
                                pygame.draw.line(game_display, red, (pos_x+5,pos_y+5), (pos_x+45,pos_y+45),5)
                                pygame.draw.line(game_display, red, (pos_x+5,pos_y+45), (pos_x+45,pos_y+5),5)

                            if not Crosses:
                                # Only Undo button if it is a cross (because it's naughts turn, so last thing placed was a cross)
                                squares, Crosses = UndoCrosses(squares, Crosses, LX, LY, MX, MY, pos_x, pos_y)

                # Check if any big squares have been won
                NandC = HasMiniGameWon(squares,LX,LY,NandC)

                if NandC[LX][LY] == 'Crosses': # if large box has been won by crosses
                    # left-top to right-bottom
                    pygame.draw.line(game_display, red, (LX*(150+es)+2*es,LY*(150+es)+4*es), ((LX+1)*(150+es)-3*es,(LY+1)*(150+es)-es),5)
                    pygame.draw.line(game_display, red, (LX*(150+es)+4*es,LY*(150+es)+2*es), ((LX+1)*(150+es)-es,(LY+1)*(150+es)-3*es),5)
                    # right-bottom to left-top
                    pygame.draw.line(game_display, red, (LX*(150+es)+4*es,(LY+1)*(150+es)-es), ((LX+1)*(150+es)-es,LY*(150+es)+4*es),5)
                    pygame.draw.line(game_display, red, (LX*(150+es)+2*es,(LY+1)*(150+es)-3*es), ((LX+1)*(150+es)-3*es,LY*(150+es)+2*es),5)

                elif NandC[LX][LY] == 'Naughts': # if large box has been won by naughts
                    pygame.draw.circle(game_display, blue, (LX*(150+es)+es+75,LY*(150+es)+es+75), 70, 5)
                    pygame.draw.circle(game_display, blue, (LX*(150+es)+es+75,LY*(150+es)+es+75), 55, 5)

        pygame.display.update()
        clock.tick(ticker)

        winner = check_if_gameover(NandC)

mainmenu_loop()
