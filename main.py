# main.py
import pygame, data, assets.gui.gui as gui, random as rnd

# setup game environment
from pygame.locals import *
pygame.init(); gameFramerate = pygame.time.Clock()
gameWindow = pygame.display.set_mode((data.SCREEN_WIDTH, data.SCREEN_HEIGHT))
pygame.display.set_caption('GridRPG -dev')

# draw background
gameWindow.blit(gui.Background0().surf, gui.Background0().rect)
board_back0 = pygame.Surface((320, 240))
board_back0.fill((83, 125, 117))
gameWindow.blit(board_back0, (160, 145))

gridComparePos = {
    # column one
    '1_xpos': (160, 224),
    '11': {
        'ypos': (125, 189),
        'clicked': False,
    '12': {
        'ypos': (189, 253),
        'clicked': False,
    '13': {
        'ypos': (253, 317),
        'clicked': False,
    '14': {
        'ypos': (317, 381),
        'clicked': False,
    # column two 
    '2_xpos': (224, 288),
    '21': {
        'ypos': (125, 189),
        'clicked': False,
    '22': {
        'ypos': (189, 253),
        'clicked': False,
    '23': {
        'ypos': (253, 317),
        'clicked': False,
    '24': {
        'ypos': (317, 381),
        'clicked': False,
    # column two 
    '2_xpos': (224, 288),
    '21': {
        'ypos': (125, 189),
        'clicked': False,
    '22': {
        'ypos': (189, 253),
        'clicked': False,
    '23': {
        'ypos': (253, 317),
        'clicked': False,
    '24': {
        'ypos': (317, 381),
        'clicked': False,
    }
    }
    }
    }
}
# draw grid
for sprite_pos in data.gridCoords:
    gameWindow.blit(gui.Square0().surf, data.gridCoords[sprite_pos])

# main loop
gameRunning = True
while gameRunning == True and data.gameTurns > 0:
    gameFramerate.tick(30)   

    pygame.display.flip()

    # game event queue
    for event in pygame.event.get():

        # quit on ESCAPE key or window close
        if event.type == KEYDOWN:
            # on ESCAPE key
            if event.key == K_ESCAPE:
                gameRunning = False
        # on mouse click
        elif event.type == QUIT:
            gameRunning = False
        # change grid image based on mouse position
        elif event.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # prepare random item or monster on click
            rndChoice = rnd.randrange(0, 5)
            if rndChoice == 1:
                loadImage = gui.Square0n()
            elif rndChoice == 2:
                loadImage = gui.Square0i()
            elif rndChoice == 3:
                loadImage = gui.Square0m()   
            elif rndChoice == 4:
                loadImage = gui.Square0n()

            # check mouse position in FIRST column
            if (mx >= 160) and (mx <= 224) and (my >= 125 and my <= 189):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (160, 125))         
            elif (mx >= 160) and (mx <= 224) and (my >= 189 and my <= 253):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (160, 189))
            elif (mx >= 160) and (mx <= 224) and (my >= 253 and my <= 317):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (160, 253))
            elif (mx >= 160) and (mx <= 224) and (my >= 317 and my <= 381):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (160, 317))

            # check SECOND column
            if (mx >= 224) and (mx <= 288) and (my >= 125 and my <= 189):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (224, 125))
            elif (mx >= 224) and (mx <= 288) and (my >= 189 and my <= 253):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (224, 189))
            elif (mx >= 224) and (mx <= 288) and (my >= 253 and my <= 317):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (224, 253))
            elif (mx >= 224) and (mx <= 288) and (my >= 317 and my <= 381):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (224, 317))
                
            # check THRID column
            if (mx >= 288) and (mx <= 352) and (my >= 125 and my <= 189):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (288, 125))
            elif (mx >= 288) and (mx <= 352) and (my >= 189 and my <= 253):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (288, 189))
            elif (mx >= 288) and (mx <= 352) and (my >= 253 and my <= 317):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (288, 253))
            elif (mx >= 288) and (mx <= 352) and (my >= 317 and my <= 381):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (288, 317))

            # check FORTH column
            if (mx >= 352) and (mx <= 416) and (my >= 125 and my <= 189):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (352, 125))
            elif (mx >= 352) and (mx <= 416) and (my >= 189 and my <= 253):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (352, 189))
            elif (mx >= 352) and (mx <= 416) and (my >= 253 and my <= 317):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (352, 253))
            elif (mx >= 352) and (mx <= 416) and (my >= 317 and my <= 381):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (352, 317))
                
            # check FIFTH column
            if (mx >= 416) and (mx <= 480) and (my >= 125 and my <= 189):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (416, 125))
            elif (mx >= 416) and (mx <= 480) and (my >= 189 and my <= 253):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (416, 189))
            elif (mx >= 416) and (mx <= 480) and (my >= 253 and my <= 317):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (416, 253))
            elif (mx >= 416) and (mx <= 480) and (my >= 317 and my <= 381):
                data.gameTurns -= 1
                gameWindow.blit(loadImage.surf, (416, 317))