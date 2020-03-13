# grid-master/main.py
import pygame, data, random as rnd

from pygame.locals import *
pygame.init(); pygame.font.init(); 
gameWindow = pygame.display.set_mode((640, 480)); 
gameFramerate = pygame.time.Clock()
pygame.display.set_caption('Gridwerks -dev')
gameFont = pygame.font.Font('assets/font/ARCADECLASSIC.TTF', 18)

sprTheme = data.sprTheme0
background = data.background0
gridData = data.gridData
gridCoords = data.gridCoords
objectList = data.objectList
gameTurns = data.gameTurns
playerHealth = data.playerHealth

def randomize_objects():
    rnd.shuffle(objectList)
    for gridPos, obj in zip(gridData, objectList):
        gridData[gridPos][3] = obj

class GridObj(pygame.sprite.Sprite):
    def __init__(self, image, flag, position = (0, 0)):
        self.image = image
        self.flag = flag
        self.position = position

    def set_flag (self):
        gridData[loc][2] = self.flag

    def draw(self, surface, position):
        surface.blit(self.image, position)

randomize_objects()
defaultSq = GridObj(sprTheme['default0'], 'can_click')
emptySq = GridObj(sprTheme['empty0'], 'no_click')
exitSq = GridObj(sprTheme['exit0'], 'can_click')
itemSq = GridObj(sprTheme['item0'], 'can_click')
enemySq = GridObj(sprTheme['enemy0'], 'can_click')
bossSq = GridObj(sprTheme['boss0'], 'can_click')

gameWindow.blit(background.convert(), (0, 0))
for spr in gridCoords:
    gameWindow.blit(defaultSq.image.convert(), gridCoords[spr])

gameRunning = True
while gameRunning == True and gameTurns > 0:
    gameFramerate.tick(30)

    guiTurns = gameFont.render(f'{gameTurns} turns  left', False, (178, 93, 77))
    guiHealth = gameFont.render(f'{playerHealth} hp  left', False, (178, 93, 77))
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                gameRunning = False
        elif event.type == pygame.QUIT:
                gameRunning = False
 
        elif event.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
               
            for loc in gridData:
                if mx in range(gridData[loc][0][0], gridData[loc][0][1]) and my in range(gridData[loc][1][0], gridData[loc][1][1]) and gridData[loc][2] == 'can_click':
                    gameTurns -= 1
                    if gridData[loc][3] == 0:
                        emptySq.draw(gameWindow, gridCoords[loc]); emptySq.set_flag()             
                    if gridData[loc][3] == 1:
                        exitSq.draw(gameWindow, gridCoords[loc]); exitSq.set_flag()
                    if gridData[loc][3] == 2:
                        bossSq.draw(gameWindow, gridCoords[loc]); bossSq.set_flag()
                    if gridData[loc][3] == 3:
                        enemySq.draw(gameWindow, gridCoords[loc]); enemySq.set_flag()
                    if gridData[loc][3] == 4:
                        itemSq.draw(gameWindow, gridCoords[loc]); itemSq.set_flag()
       
    gameWindow.fill((103, 145, 137), (160, 380, 400, 14))
    gameWindow.blit(guiTurns, (170, 380))
    gameWindow.blit(guiHealth, (385, 380))
    pygame.display.flip()
