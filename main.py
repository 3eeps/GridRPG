# grid-master/main.py
import pygame, data, random as rnd

# build game environment
from pygame.locals import *
pygame.init(); gameFramerate = pygame.time.Clock()
gameWindow = pygame.display.set_mode((data.SCREEN_WIDTH, data.SCREEN_HEIGHT))
pygame.display.set_caption('GridRPG -dev')

sprites = data.sprites
ranges = data.ranges
coords = data.coords
gameWindow.blit(sprites['background0'], (0, 0))
for sprite_pos in data.coords:
    gameWindow.blit(sprites['square0'].convert(), coords[sprite_pos])

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
            
            for col in ranges:
                if mx in range(ranges[col][0][0], ranges[col][0][1]) and my in range(ranges[col][1][0], ranges[col][1][1]) and ranges[col][2] == 0:
                    ranges[col][2] = 1
                    gameWindow.blit(data.spriteList[rnd.randrange(0, 3)], coords[col])

    pygame.display.flip()
