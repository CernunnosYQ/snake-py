import numpy as np
import random


class Stage:
    ''' Clase que maneja el escenario 

    Funciona con una matriz para el estado de juego, con 3 se marca la posicion de los
    muros, con 2 la comida y con 1 la posicion de la serpiente.

    '''

    def __init__(self, cells_x: int, cells_y: int):
        '''Inicializa el escenario

        Definimos las variables locales y las dimensiones de nuestro juego. Creamos
        la matriz de nuestro escenario y definimos la ubicacion de la primer comida.

        '''
        self.cells_x = cells_x
        self.cells_y = cells_y

        self.speed = 1

        self.state = np.zeros((cells_x, cells_y))
        for y in range(self.cells_y):
            for x in range(self.cells_x):
                if any((y == 0, x == 0, y == self.cells_y - 1, x == self.cells_x - 1)):
                    self.state[x, y] = 3

        self.food = (random.randrange(1, cells_x - 1),
                     random.randrange(1, cells_y - 1))
        self.state[self.food] = 2

    def get_cell(self, x, y):
        return self.state[x, y]

    def get_speed(self):
        return self.speed

    def update_state(self, player):
        ''' Actualiza el estado del escenario

        Crea una matriz con las dimensiones del esenario iniciada en 0 despues escribe
        sobre esta la posicion de la comida y el jugador.

        '''
        new_state = np.zeros((self.cells_x, self.cells_y))

        for y in range(self.cells_y):
            for x in range(self.cells_x):
                if any((y == 0, x == 0, y == self.cells_y - 1, x == self.cells_x - 1)):
                    new_state[x, y] = 3

        new_state[self.food] = 2

        player.move()

        for pos in player.get_position():
            new_state[pos[0], pos[1]] = 1

        self.state = new_state

        return self.colisions(player)

    def create_food(self):
        ''' Reubicar la comida cada que la serpiente la consigue

        '''
        self.food = (random.randrange(1, self.cells_x - 1),
                     random.randrange(1, self.cells_y - 1))

    def colisions(self, player):
        ''' Detector de colisiones

        '''
        head_position = player.get_position()[0]

        if any((player.biting_tail(), head_position[0] == 0, head_position[0] == self.cells_x - 1,
                head_position[1] == 0, head_position[1] == self.cells_y - 1)):
            print('Choco con el muro')
            return True
        elif all(head_position == self.food):
            self.create_food()
            self.speed += 0.1
            player.give_food()

        return False
