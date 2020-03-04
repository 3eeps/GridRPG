# main.py
import pygame, assets.gui.gui as gui

# setup game environment
from pygame.locals import *
pygame.init(); gameFramerate = pygame.time.Clock()
gameWindow = pygame.display.set_mode((640, 480))
pygame.display.set_caption('GridRPG -dev')

# draw background
gameWindow.blit(gui.Background0().surf, gui.Background0().rect)
board_back0 = pygame.Surface((320, 240))
board_back0.fill((83, 125, 117))
gameWindow.blit(board_back0, (160, 145))

# draw grid
gridCol01 = {'11': (160, 125), '12': (160, 189), '13': (160, 253), '14': (160, 317)}
gridCol02 = {'21': (224, 125), '22': (224, 189), '23': (224, 253), '24': (224, 317)}
gridCol03 = {'31': (288, 125), '32': (288, 189), '33': (288, 253), '34': (288, 317)}
gridCol04 = {'41': (352, 125), '42': (352, 189), '43': (352, 253), '44': (352, 317)}
gridCol05 = {'51': (416, 125), '52': (416, 189), '53': (416, 253), '54': (416, 317)}

for sprite_pos in gridCol01:
    gameWindow.blit(gui.Square0().surf, gridCol01[sprite_pos])

for sprite_pos in gridCol02:
    gameWindow.blit(gui.Square0().surf, gridCol02[sprite_pos])

for sprite_pos in gridCol03:
    gameWindow.blit(gui.Square0().surf, gridCol03[sprite_pos])

for sprite_pos in gridCol04:
    gameWindow.blit(gui.Square0().surf, gridCol04[sprite_pos])

for sprite_pos in gridCol05:
    gameWindow.blit(gui.Square0().surf, gridCol05[sprite_pos])

# main loop
clicked = False
gameRunning = True
while gameRunning == True:
    gameFramerate.tick(30)   

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
        # change grid image based on mouse position
        elif event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                # check mouse position in first column
                if (mx >= 160) and (mx <= 224) and (my >= 125 and my <= 189):
                    gameWindow.blit(gui.Square02().surf, (160, 125))
                elif (mx >= 160) and (mx <= 224) and (my >= 189 and my <= 253):
                    gameWindow.blit(gui.Square02().surf, (160, 189))
                elif (mx >= 160) and (mx <= 224) and (my >= 253 and my <= 317):
                    gameWindow.blit(gui.Square02().surf, (160, 253))
                elif (mx >= 160) and (mx <= 224) and (my >= 317 and my <= 381):
                    gameWindow.blit(gui.Square02().surf, (160, 317))

                # check mouse position in second column
                if (mx >= 224) and (mx <= 288) and (my >= 125 and my <= 189):
                    gameWindow.blit(gui.Square02().surf, (224, 125))
                elif (mx >= 224) and (mx <= 288) and (my >= 189 and my <= 253):
                    gameWindow.blit(gui.Square02().surf, (224, 189))
                elif (mx >= 224) and (mx <= 288) and (my >= 253 and my <= 317):
                    gameWindow.blit(gui.Square02().surf, (224, 253))
                elif (mx >= 224) and (mx <= 288) and (my >= 317 and my <= 381):
                    gameWindow.blit(gui.Square02().surf, (224, 317))
                
                # check mouse position in third column
                #check mouse position in second column
                if (mx >= 288) and (mx <= 352) and (my >= 125 and my <= 189):
                    gameWindow.blit(gui.Square02().surf, (224, 125))
                elif (mx >= 288) and (mx <= 352) and (my >= 189 and my <= 253):
                    gameWindow.blit(gui.Square02().surf, (224, 189))
                elif (mx >= 288) and (mx <= 352) and (my >= 253 and my <= 317):
                    gameWindow.blit(gui.Square02().surf, (224, 253))
                elif (mx >= 288) and (mx <= 352) and (my >= 317 and my <= 381):
                    gameWindow.blit(gui.Square02().surf, (224, 317))