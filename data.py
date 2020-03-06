# grid.py

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

gameTurns = 256

Coords = {
# column 1
    '11': (160, 125),
    '12': (160, 189),
    '13': (160, 253), 
    '14': (160, 317),
# column 2
    '21': (224, 125), 
    '22': (224, 189), 
    '23': (224, 253), 
    '24': (224, 317),
# column 3
    '31': (288, 125), 
    '32': (288, 189), 
    '33': (288, 253), 
    '34': (288, 317),
# column 4
    '41': (352, 125), 
    '42': (352, 189), 
    '43': (352, 253), 
    '44': (352, 317),
# column 5    
    '51': (416, 125), 
    '52': (416, 189), 
    '53': (416, 253), 
    '54': (416, 317)
}

gridInfo = {
# column 1
    11: {'xy_pos': [(160, 224), (125, 189), 0]},
    12: {'xy_pos': [(160, 224), (189, 253), 0]},
    13: {'xy_pos': [(160, 224), (253, 317), 0]},
    14: {'xy_pos': [(160, 224), (317, 381), 0]},
# column 2
    21: {'xy_pos': [(224, 288), (125, 189), 0]},
    22: {'xy_pos': [(224, 288), (189, 253), 0]},
    23: {'xy_pos': [(224, 288), (253, 317), 0]},
    24: {'xy_pos': [(224, 288), (317, 381), 0]},
# column 3 
    31: {'xy_pos': [(288, 352), (125, 189), 0]},
    32: {'xy_pos': [(288, 352), (189, 253), 0]},
    33: {'xy_pos': [(288, 352), (253, 317), 0]},
    34: {'xy_pos': [(288, 352), (317, 381), 0]},
# column 4 
    41: {'xy_pos': [(352, 416), (125, 189), 0]},
    42: {'xy_pos': [(352, 416), (189, 253), 0]},
    43: {'xy_pos': [(352, 416), (253, 317), 0]},
    44: {'xy_pos': [(352, 416), (317, 381), 0]},
# column 5 
    51: {'xy_pos': [(416, 480), (125, 189), 0]},
    52: {'xy_pos': [(416, 480), (189, 253), 0]},
    53: {'xy_pos': [(416, 480), (253, 317), 0]},
    54: {'xy_pos': [(416, 480), (317, 381), 0]},
}   