from enums.moves import Moves


BOARD_SIZE = 3

VALID_POSITIONS = {
    1 : [0,0],
    2 : [0,1],
    3 : [0,2],
    4 : [1,0],
    5 : [1,1],
    6 : [1,2],
    7 : [2,0],
    8 : [2,1],
    9 : [2,2]
}

VALID_COORDINATES_TO_POSITIONS = {
    (0,0) : 1,
    (0,1) : 2,
    (0,2) : 3,
    (1,0) : 4,
    (1,1) : 5,
    (1,2) : 6,
    (2,0) : 7,
    (2,1) : 8,
    (2,2) : 9
}

TALLYS = {
    Moves.X.value : 1,
    Moves.O.value : -1
}