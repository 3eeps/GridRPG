# main.py

# modules
import pygame, assets.gui.gui as gui

# control library
from pygame.locals import *

# initialize game environment
pygame.init(); gameFramerate = pygame.time.Clock()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('GridRPG -dev')

# main loop
gameRunning = True
while gameRunning == True:
    gameFramerate.tick(60)

    # event queue
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
            if board_back0_rect.rect.collidepoint(pygame.mouse.get_pos()):
                print('TEST')
                   
    # render background and grid
    gameWindow.blit(gui.Background0().surf, gui.Background0())
    board_back0 = pygame.Surface((320, 240))
    board_back0_rect = board_back0.get_rect()
    board_back0.fill((83, 125, 117))
    gameWindow.blit(board_back0, (160, 145))

    # draw grid over board_back0 rect
    for x in range(0, 8):
        for y in range(0, 6):
            gameWindow.blit(gui.Square0().surf, ((x + 4) * 40, (y + 3) * 42))

    pygame.display.flip()
