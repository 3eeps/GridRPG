# gridrpg-master/data.py
import pygame, random as rnd

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

gameTurns = 256
objectData = {
    'emptySpace': (10, 0),
    'exitDoor': (1, 1),
    'bosses': (1, 2),
    'enemies': (5, 3),
    'items': (3, 4)  
}

objectList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 3, 3, 3, 3, 4, 4, 4]

def place_objects():
    rnd.shuffle(objectList)
    for square in gridData:
        for object in objectList:
            gridData[square][3] = objectList[object]

sprTheme0 = {

    'background0': pygame.image.load('assets/images/0/background0.png'),
    'square0': pygame.image.load('assets/images/0/square0.png'),
    'empty0': pygame.image.load('assets/images/0/square0n.png'),
    'exit0': pygame.image.load('assets/images/0/square0e.png'),
    'item0': pygame.image.load('assets/images/0/square0i.png'),
    'enemy0': pygame.image.load('assets/images/0/square0m.png'),
    'boss0': pygame.image.load('assets/images/0/square0b.png')
}

spriteList0 = [sprTheme0['empty0'], sprTheme0['exit0'], sprTheme0['item0'], sprTheme0['enemy0'], sprTheme0['boss0']]

gridCoords = {
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

gridData = {
# column 1
11: [(160, 224), (125, 189), 0, 0],
12: [(160, 224), (189, 253), 0, 0],
13: [(160, 224), (253, 317), 0, 0],
14: [(160, 224), (317, 381), 0, 0],
# column 2
21: [(224, 288), (125, 189), 0, 0],
22: [(224, 288), (189, 253), 0, 0],
23: [(224, 288), (253, 317), 0, 0],
24: [(224, 288), (317, 381), 0, 0],
# column 3 
31: [(288, 352), (125, 189), 0, 0],
32: [(288, 352), (189, 253), 0, 0],
33: [(288, 352), (253, 317), 0, 0],
34: [(288, 352), (317, 381), 0, 0],
# column 4 
41: [(352, 416), (125, 189), 0, 0],
42: [(352, 416), (189, 253), 0, 0],
43: [(352, 416), (253, 317), 0, 0],
44: [(352, 416), (317, 381), 0, 0],
# column 5 
51: [(416, 480), (125, 189), 0, 0],
52: [(416, 480), (189, 253), 0, 0],
53: [(416, 480), (253, 317), 0, 0],
54: [(416, 480), (317, 381), 0, 0]
}