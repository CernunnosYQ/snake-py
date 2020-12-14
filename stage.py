import numpy as np
import random


class Stage:
    ''' Clase que maneja el escenario 

    Funciona con una matriz para el estado de juego, con 2 se marca la posicion de la
    comida y con 1 la posicion de la serpiente.

    '''
    def __init__(self, cells_x: int, cells_y: int):
        '''Inicializa el escenario

        Definimos las variables locales y las dimensiones de nuestro juego. Creamos
        la matriz de nuestro escenario y definimos la ubicacion de la primer comida.

        '''
        self.cells_x = cells_x
        self.cells_y = cells_y

        print(self.cells_x, self.cells_y)

        self.state = np.zeros((cells_x, cells_y))

        self.food = (random.randrange(cells_x), random.randrange(cells_y))
        self.state[self.food] = 2

        print(self.food)
        print(self.state)

    def update_state(self):
        ''' Actualiza el estado del escenario
        
        Crea una matriz con las dimensiones del esenario iniciada en 0 despues escribe
        sobre esta la posicion de la comida y el jugador.

        '''
        new_state = np.zeros((self.cells_x, self.cells_y))
        new_state[self.food] = 1

        self.state = new_state
        print(self.state)

    def create_food(self):
        ''' Crear comida

        Esta función se encarga de crear o más bien de reubicar la comida cada que el
        jugador la consigue.

        '''
        self.food = (random.randrange(self.cells_x), random.randrange(self.cells_y))
        print(self.food)
        self.update_state()

