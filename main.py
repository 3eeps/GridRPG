# grid-master/main.py
import pygame, data, random as rnd

from pygame.locals import *
pygame.init(); pygame.font.init(); 
gameWindow = pygame.display.set_mode((640, 480)); 
gameFramerate = pygame.time.Clock()
pygame.display.set_caption('Gridwerks -dev')
gameFont = pygame.font.Font('assets/font/ARCADECLASSIC.TTF', 18)

sprTheme0 = data.sprTheme0
gridData = data.gridData
gridCoords = data.gridCoords
objectList = data.objectList
gameTurns = data.gameTurns
playerHealth = data.playerHealth

def randomize_objects():
    rnd.shuffle(objectList)
    for gridPos, obj in zip(gridData, objectList):
        gridData[gridPos][3] = obj

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, image, flag):
        self.image = image
        self.flag = flag
        self.surf = image.get_rect()

    def set_flag (self):
        if self.flag == 'clickable':
            self.flag = 0
        elif self.flag == 'noclick':
            self.flag = 1
        elif self.flag == 'item' or 'enemy' or 'exit':
            self.flag == 2

randomize_objects()
sprite0 = Sprite(sprTheme0['default0'], 'clickable')

gameWindow.blit(data.background0.convert(), (0, 0))
for spr in gridCoords:
    gameWindow.blit(sprite0.image, gridCoords[spr])

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
                if mx in range(gridData[loc][0][0], gridData[loc][0][1]) and my in range(gridData[loc][1][0], gridData[loc][1][1]) and gridData[loc][2] == 0:
                    gridData[loc][2] = 1
                    gameTurns -= 1
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
       
    gameWindow.fill((103, 145, 137), (160, 380, 400, 14))
    gameWindow.blit(guiTurns, (170, 380))
    gameWindow.blit(guiHealth, (385, 380))
    pygame.display.flip()
