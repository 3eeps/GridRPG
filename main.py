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
for sprite_pos in data.Grid.Coords:
    gameWindow.blit(gui.Square0().surf, data.Grid.Coords[sprite_pos])

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
            compareDict = data.Grid.comparePos

            for _ in compareDict:
                if mx >= compareDict['11']['xy_pos'][[0]]:
                    print ('click')

