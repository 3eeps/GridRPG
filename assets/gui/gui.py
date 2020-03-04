# assets/gui/gui.py
import pygame

class Background0(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.image.load("assets/gui/themes/dungeon_back0.png")
        self.rect = self.surf.get_rect()

class Square0(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.image.load("assets/gui/themes/square0.png")
        self.rect = self.surf.get_rect()

class Square0i(pygame.sprite.Sprite):
    def __init__(self):       
        self.surf = pygame.image.load("assets/gui/themes/square0i.png")
        self.rect = self.surf.get_rect()

class Square0m(pygame.sprite.Sprite):
    def __init__(self):       
        self.surf = pygame.image.load("assets/gui/themes/square0m.png")
        self.rect = self.surf.get_rect()

class Square0n(pygame.sprite.Sprite):
    def __init__(self):       
        self.surf = pygame.image.load("assets/gui/themes/square0n.png")
        self.rect = self.surf.get_rect()
