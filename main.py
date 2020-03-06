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
for sprite_pos in data.Coords:
    gameWindow.blit(gui.Square0().surf, data.Coords[sprite_pos])

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

            for square_id, data in data.gridInfo.items():
                mx, my = pygame.mouse.get_pos()
                for key in data:                  
                    x1 = data[key][0][0]; x2 = data[key][0][1]                   
                    y1 = data[key][1][0]; y2 = data[key][1][1]
                    flag = data[key][2]
                    if mx in range(x1, x2) and my in range(y1, y2):
                        print(flag)
