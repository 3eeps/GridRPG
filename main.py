# grid-master/main.py
import pygame, data, random as rnd

from pygame.locals import *
pygame.init(); gameFramerate = pygame.time.Clock()
gameWindow = pygame.display.set_mode((data.SCREEN_WIDTH, data.SCREEN_HEIGHT))
pygame.display.set_caption('Gridwerks -dev')

sprTheme0 = data.sprTheme0
gridData = data.gridData
gridCoords = data.gridCoords
spriteList0 = data.spriteList0

gameWindow.blit(sprTheme0['background0'].convert(), (0, 0))
for spritePos in gridCoords:
    gameWindow.blit(sprTheme0['square0'].convert(), gridCoords[spritePos])

gameRunning = True
while gameRunning == True:
    gameFramerate.tick(30)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                gameRunning = False
        elif event.type == pygame.QUIT:
                gameRunning = False

        elif event.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            for loc in gridData:
                if mx in range(gridData[loc][0][0], gridData[loc][0][1]) and my in range(gridData[loc][1][0], gridData[loc][1][1]) and gridData[loc][2] == 0:
                    gridData[loc][2] = 1
                    gameWindow.blit(spriteList0[rnd.randrange(0, 3)].convert(), gridCoords[loc])

    pygame.display.flip()
