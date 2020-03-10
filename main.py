# grid-master/main.py
import pygame, data, random as rnd

from pygame.locals import *
pygame.init(); gameFramerate = pygame.time.Clock()
gameWindow = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Gridwerks -dev')

sprTheme0 = data.sprTheme0
gridData = data.gridData
gridCoords = data.gridCoords
objectList = data.objectList

def add_objects():
    rnd.shuffle(objectList)
    for grid_key, object_value in zip(gridData, objectList):
        gridData[grid_key][3] = object_value

add_objects()
    
gameWindow.blit(sprTheme0['background0'].convert(), (0, 0))
for spr in gridCoords:
    gameWindow.blit(sprTheme0['square0'].convert(), gridCoords[spr])

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
                    if gridData[loc][3] == 0:
                        gameWindow.blit(sprTheme0['empty0'].convert(), gridCoords[loc])
                    if gridData[loc][3] == 1:
                        gameWindow.blit(sprTheme0['exit0'].convert(), gridCoords[loc])
                    if gridData[loc][3] == 2:
                        gameWindow.blit(sprTheme0['item0'].convert(), gridCoords[loc])
                    if gridData[loc][3] == 3:
                        gameWindow.blit(sprTheme0['enemy0'].convert(), gridCoords[loc])
                    if gridData[loc][3] == 4:
                        gameWindow.blit(sprTheme0['boss0'].convert(), gridCoords[loc])
                    
    pygame.display.flip()
