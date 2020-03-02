# assets/gui/gui.py

# modules
import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Background0(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.image.load("assets/gui/themes/dungeon_back0.png")
        self.rect = self.surf.get_rect()

class Square0(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.image.load("assets/gui/themes/square0.png")
        self.rect = self.surf.get_rect()

class Square02(pygame.sprite.Sprite):
    def __init__(self):       
        self.surf = pygame.image.load("assets/gui/themes/square0_click.png")
        self.rect = self.surf.get_rect()
