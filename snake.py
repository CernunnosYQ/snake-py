import numpy as np


class Snake:
    def __init__(self, coordinates, direction='right'):
        self.position = np.array([coordinates])
        self.direction = direction
        self.has_food = False

        print(self.position)

    def give_food(self):
        self.has_food = True

    def get_position(self):
        return self.position

    def move(self):
        if self.direction == 'up':
            self.position[0][1] -= 1
        elif self.direction == 'down':
            self.position[0][1] += 1
        elif self.direction == 'left':
            self.position[0][0] -= 1
        elif self.direction == 'right':
            self.position[0][0] += 1
        else:
            print('Something weird happened')

        print(self.position)

    def change_direction(self, new_direction):
        if new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'top' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction

        print(self.direction)

