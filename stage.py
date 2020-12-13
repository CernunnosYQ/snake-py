import numpy as np
import random


class Stage:
    def __init__(self, cells_x, cells_y):
        self.cells_x = cells_x
        self.cells_y = cells_y

        self.state = np.zeros((cells_x, cells_y))

        self.food = (random.randrange(cells_x), random.randrange(cells_y))
        self.state[self.food] = 1
