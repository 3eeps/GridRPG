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

# draw grid
for sprite_pos in data.Grid.coords:
    gameWindow.blit(gui.Square0().surf, data.Grid.coords[sprite_pos])



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
            rangeDict = data.Grid.ranges

            # compare mouse xy and replace image
            for col in rangeDict:
                if mx in range(rangeDict[col][0][0], rangeDict[col][0][1]) and my in range(rangeDict[col][1][0], rangeDict[col][1][1]) and rangeDict[col][2] == 0:
                    # set flag to not replace image after first click
                    rangeDict[col][2] = 1
                    # replace image with random one
                    gameWindow.blit(data.Grid.imageList[rnd.randrange(0, 4)].surf, data.Grid.coords[col])
                    
