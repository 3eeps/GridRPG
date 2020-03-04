# main.py
import pygame, assets.gui.gui as gui, random as rnd

# setup game environment
from pygame.locals import *
pygame.init(); gameFramerate = pygame.time.Clock()
gameWindow = pygame.display.set_mode((640, 480))
pygame.display.set_caption('GridRPG -dev')

# draw background
gameWindow.blit(gui.Background0().surf, gui.Background0().rect)
board_back0 = pygame.Surface((320, 240))
board_back0.fill((83, 125, 117))
gameWindow.blit(board_back0, (160, 145))

# draw grid
gridCoords = {'11': (160, 125), '12': (160, 189), '13': (160, 253), '14': (160, 317), '21': (224, 125), '22': (224, 189), '23': (224, 253), '24': (224, 317), '31': (288, 125), '32': (288, 189), '33': (288, 253), '34': (288, 317), '41': (352, 125), '42': (352, 189), '43': (352, 253), '44': (352, 317), '51': (416, 125), '52': (416, 189), '53': (416, 253), '54': (416, 317)}

for sprite_pos in gridCoords:
    gameWindow.blit(gui.Square0().surf, gridCoords[sprite_pos])

# main loop
gameRunning = True
while gameRunning == True:
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
                gameWindow.blit(loadImage.surf, (160, 125))
            elif (mx >= 160) and (mx <= 224) and (my >= 189 and my <= 253):
                gameWindow.blit(loadImage.surf, (160, 189))
            elif (mx >= 160) and (mx <= 224) and (my >= 253 and my <= 317):
                gameWindow.blit(loadImage.surf, (160, 253))
            elif (mx >= 160) and (mx <= 224) and (my >= 317 and my <= 381):
                gameWindow.blit(loadImage.surf, (160, 317))

            # check SECOND column
            if (mx >= 224) and (mx <= 288) and (my >= 125 and my <= 189):
                gameWindow.blit(loadImage.surf, (224, 125))
            elif (mx >= 224) and (mx <= 288) and (my >= 189 and my <= 253):
                gameWindow.blit(loadImage.surf, (224, 189))
            elif (mx >= 224) and (mx <= 288) and (my >= 253 and my <= 317):
                gameWindow.blit(loadImage.surf, (224, 253))
            elif (mx >= 224) and (mx <= 288) and (my >= 317 and my <= 381):
                gameWindow.blit(loadImage.surf, (224, 317))
                
            # check THRID column
            if (mx >= 288) and (mx <= 352) and (my >= 125 and my <= 189):
                gameWindow.blit(loadImage.surf, (288, 125))
            elif (mx >= 288) and (mx <= 352) and (my >= 189 and my <= 253):
                gameWindow.blit(loadImage.surf, (288, 189))
            elif (mx >= 288) and (mx <= 352) and (my >= 253 and my <= 317):
                gameWindow.blit(loadImage.surf, (288, 253))
            elif (mx >= 288) and (mx <= 352) and (my >= 317 and my <= 381):
                gameWindow.blit(loadImage.surf, (288, 317))

            # check FORTH column
            if (mx >= 352) and (mx <= 416) and (my >= 125 and my <= 189):
                gameWindow.blit(loadImage.surf, (352, 125))
            elif (mx >= 352) and (mx <= 416) and (my >= 189 and my <= 253):
                gameWindow.blit(loadImage.surf, (352, 189))
            elif (mx >= 352) and (mx <= 416) and (my >= 253 and my <= 317):
                gameWindow.blit(loadImage.surf, (352, 253))
            elif (mx >= 352) and (mx <= 416) and (my >= 317 and my <= 381):
                gameWindow.blit(loadImage.surf, (352, 317))
                
            # check FIFTH column
            if (mx >= 416) and (mx <= 480) and (my >= 125 and my <= 189):
                gameWindow.blit(loadImage.surf, (416, 125))
            elif (mx >= 416) and (mx <= 480) and (my >= 189 and my <= 253):
                gameWindow.blit(loadImage.surf, (416, 189))
            elif (mx >= 416) and (mx <= 480) and (my >= 253 and my <= 317):
                gameWindow.blit(loadImage.surf, (416, 253))
            elif (mx >= 416) and (mx <= 480) and (my >= 317 and my <= 381):
                gameWindow.blit(loadImage.surf, (416, 317))