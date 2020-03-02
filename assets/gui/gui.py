# assets/gui/gui.py

# modules
import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Background0(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("assets/gui/themes/dungeon_back0.png")
        self.rect = ((0, 0, 640, 480))

class Square0(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("assets/gui/themes/square0.png")
        self.rect = ((0, 0, 38, 40))
