import numpy as np
import random
from time import sleep

def empty_board():
    board = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    return(board)

print(empty_board())