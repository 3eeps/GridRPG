# main.py

# modules
import pygame, assets.gui.gui as gui

# library for game controls
from pygame.locals import *

# setup game environment
pygame.init(); gameFramerate = pygame.time.Clock()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('GridRPG -dev')

clicked = False

# render background and grid
gameWindow.blit(gui.Background0().surf, gui.Background0().rect)
board_back0 = pygame.Surface((320, 240))
board_back0.fill((83, 125, 117))
gameWindow.blit(board_back0, (160, 145))

for x in range(0, 5):
    for y in range(0, 4):
        gameWindow.blit(gui.Square0().surf, ((x + 2.5) * 64, (y + 2) * 64))

# main loop
gameRunning = True
while gameRunning == True:
    gameFramerate.tick(60)

    if clicked == True:
        clicked_square02 = gui.Square02()
        gameWindow.blit(clicked_square02.surf, clicked_square02)   

    pygame.display.flip()

    # game event queue
    for event in pygame.event.get():

        # quit on ESCAPE key or window close
        if event.type == KEYDOWN:
            # ESCAPE key
            if event.key == K_ESCAPE:
                gameRunning = False
        # mouse window close
        elif event.type == QUIT:
            gameRunning = False
        # build_ change texture on MOUSEBUTTONDOWN
        elif event.type == MOUSEBUTTONDOWN:
            square = gui.Square0()
            if square.rect.collidepoint(pygame.mouse.get_pos()):
                clicked = True
                print('TEST')
