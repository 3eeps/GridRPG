# grid-master/main.py
import pygame, data, functions as func

from pygame.locals import *
pygame.init(); pygame.font.init(); 
gameWindow = pygame.display.set_mode((640, 480)); 
gameFramerate = pygame.time.Clock()
pygame.display.set_caption('Gridwerks -dev')
gameFont = pygame.font.Font('assets/font/ARCADECLASSIC.TTF', 16)

sprTheme0 = data.sprTheme0
gridData = data.gridData
gridCoords = data.gridCoords
objectList = data.objectList
gameTurns = data.gameTurns

func.randomize_objects()

gameWindow.blit(sprTheme0['background0'].convert(), (0, 0))
for spr in gridCoords:
    gameWindow.blit(sprTheme0['square0'].convert(), gridCoords[spr])

turnText = gameFont.render(f'{gameTurns} turns left', False, (178, 93, 77))

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
            gameTurns -= 1
            gameWindow.blit(turnText, (160, 110))
            
            for loc in gridData:
                if mx in range(gridData[loc][0][0], gridData[loc][0][1]) and my in range(gridData[loc][1][0], gridData[loc][1][1]) and gridData[loc][2] == 0:
                    gridData[loc][2] = 1
                    if gridData[loc][3] == 0:
                        gameWindow.blit(sprTheme0['empty0'].convert(), gridCoords[loc])
                    if gridData[loc][3] == 1:
                        gameWindow.blit(sprTheme0['exit0'].convert(), gridCoords[loc])
                    if gridData[loc][3] == 2:
                        gameWindow.blit(sprTheme0['boss0'].convert(), gridCoords[loc])
                    if gridData[loc][3] == 3:
                        gameWindow.blit(sprTheme0['enemy0'].convert(), gridCoords[loc])
                    if gridData[loc][3] == 4:
                        gameWindow.blit(sprTheme0['item0'].convert(), gridCoords[loc])
       
    gameWindow.blit(turnText, (160, 110))
    pygame.display.flip()
