# gridrpg-master/data.py
from pygame import image, sprite

gameTurns = 256
playerHealth = 100
background0 = image.load('assets/images/0/background0.png')

sprTheme0 = {
'default0': image.load('assets/images/0/square0.png'),
'empty0': image.load('assets/images/0/square0n.png'),
'exit0': image.load('assets/images/0/square0e.png'),
'item0': image.load('assets/images/0/square0i.png'),
'enemy0': image.load('assets/images/0/square0m.png'),
'boss0': image.load('assets/images/0/square0b.png')}


# emptyspace: 0, exitdoor: 1, bosses: 2, enemies: 3, items: 4
objectList = [0, 0, 0, 0, 0, 1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 0, 0, 0, 0, 0]

gridCoords = {
11: (160, 125),
12: (160, 189),
13: (160, 253),
14: (160, 317),

21: (224, 125),
22: (224, 189),
23: (224, 253),
24: (224, 317),

31: (288, 125), 
32: (288, 189), 
33: (288, 253), 
34: (288, 317),

41: (352, 125),
42: (352, 189),
43: (352, 253),
44: (352, 317),
   
51: (416, 125), 
52: (416, 189),
53: (416, 253),
54: (416, 317)}

gridData = {
11: [(160, 224), (125, 189), 'can_click', 0],
12: [(160, 224), (189, 253), 'can_click', 0],
13: [(160, 224), (253, 317), 'can_click', 0],
14: [(160, 224), (317, 381), 'can_click', 0],

21: [(224, 288), (125, 189), 'can_click', 0],
22: [(224, 288), (189, 253), 'can_click', 0],
23: [(224, 288), (253, 317), 'can_click', 0],
24: [(224, 288), (317, 381), 'can_click', 0],

31: [(288, 352), (125, 189), 'can_click', 0],
32: [(288, 352), (189, 253), 'can_click', 0],
33: [(288, 352), (253, 317), 'can_click', 0],
34: [(288, 352), (317, 381), 'can_click', 0],

41: [(352, 416), (125, 189), 'can_click', 0],
42: [(352, 416), (189, 253), 'can_click', 0],
43: [(352, 416), (253, 317), 'can_click', 0],
44: [(352, 416), (317, 381), 'can_click', 0],
 
51: [(416, 480), (125, 189), 'can_click', 0],
52: [(416, 480), (189, 253), 'can_click', 0],
53: [(416, 480), (253, 317), 'can_click', 0],
54: [(416, 480), (317, 381), 'can_click', 0]}
