# grid-master/functions.py
from random import shuffle
from data import objectList, gridData

def randomize_objects():
    shuffle(objectList)
    for gridPos, obj in zip(gridData, objectList):
        gridData[gridPos][3] = obj

class Sprite(pygame.sprite.Sprite):
    def __init__(self, position, image, type, flag):

        self.item = 
        self.position = position
