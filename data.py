# grid.py
import pygame, random as rnd

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

gameTurns = 256

# sprite variables
class Sprites0(): 

    background0 = pygame.image.load('assets/images/0/background0.png')
    square0 = pygame.image.load('assets/images/0/square0.png')
    square0n = pygame.image.load('assets/images/0/square0n.png')
    square0e = pygame.image.load('assets/images/0/square0e.png')
    square0i = pygame.image.load('assets/images/0/square0i.png')
    square0m = pygame.image.load('assets/images/0/square0m.png')
    square0b = pygame.image.load('assets/images/0/square0b.png')

    # Sprites listed for grid
    imgList = [square0n, square0e, square0i, square0m, square0b]

class Grid():

    def randomizeSquares():
        items = rnd.randrange(2, 3)
        monsters = rnd.randrange(3, 5)
        bosses = rnd.randrange(1, 2)
        empty = rnd.randrange(5, 10)
        exit_door = 1

        total = items + monsters + bosses + empty + exit_door
        if total > 20:
            randomizeSquares()
        else:
            return total

    coords = {
    # column 1
        11: (160, 125),
        12: (160, 189),
        13: (160, 253), 
        14: (160, 317),
    # column 2
        21: (224, 125), 
        22: (224, 189), 
        23: (224, 253), 
        24: (224, 317),
    # column 3
        31: (288, 125), 
        32: (288, 189), 
        33: (288, 253), 
        34: (288, 317),
    # column 4
        41: (352, 125), 
        42: (352, 189), 
        43: (352, 253), 
        44: (352, 317),
    # column 5    
        51: (416, 125), 
        52: (416, 189), 
        53: (416, 253), 
        54: (416, 317)
}

    ranges = {
    # column 1
        11: [(160, 224), (125, 189), 0],
        12: [(160, 224), (189, 253), 0],
        13: [(160, 224), (253, 317), 0],
        14: [(160, 224), (317, 381), 0],
    # column 2
        21: [(224, 288), (125, 189), 0],
        22: [(224, 288), (189, 253), 0],
        23: [(224, 288), (253, 317), 0],
        24: [(224, 288), (317, 381), 0],
    # column 3 
        31: [(288, 352), (125, 189), 0],
        32: [(288, 352), (189, 253), 0],
        33: [(288, 352), (253, 317), 0],
        34: [(288, 352), (317, 381), 0],
    # column 4 
        41: [(352, 416), (125, 189), 0],
        42: [(352, 416), (189, 253), 0],
        43: [(352, 416), (253, 317), 0],
        44: [(352, 416), (317, 381), 0],
    # column 5 
        51: [(416, 480), (125, 189), 0],
        52: [(416, 480), (189, 253), 0],
        53: [(416, 480), (253, 317), 0],
        54: [(416, 480), (317, 381), 0],
} 

print(Grid.randomizeSquares())
