import numpy as np


class Snake:
    def __init__(self, pos_x, pos_y):
        self.position = np.array([[pos_x, pos_y], [pos_x - 1, pos_y]])
        self.direction = 'right'
        self.has_food = False

    def give_food(self):
        ''' Alimenta a la serpiente para que crezca

        '''

        self.has_food = True

    def get_position(self):
        ''' Retorna el array de posiciones de la serpiente

        '''

        return self.position

    def move(self):
        ''' Cambiar la posicion de la serpiente

        Inserta al comienzo del array un nuevo valor para la cabeza de la serpiente
        las coordenadas para este nuevo punto dependen de la dirección en que se
        dirige la serpiente.

        Al final con la variable 'has_food' distingue si la serpiente tiene comida
        y en caso de que no, elimina el ultimo item del array de posiciones para que
        la serpiente mantenga su longitud.

        '''

        if self.direction == 'up':
            self.position = np.concatenate((
                [[self.position[0, 0], self.position[0][1] - 1]], self.position))
        elif self.direction == 'down':
            self.position = np.concatenate((
                [[self.position[0][0], self.position[0][1] + 1]], self.position))
        elif self.direction == 'left':
            self.position = np.concatenate((
                [[self.position[0][0] - 1, self.position[0][1]]], self.position))
        elif self.direction == 'right':
            self.position = np.concatenate((
                [[self.position[0][0] + 1, self.position[0][1]]], self.position))

        if not self.has_food:
            self.position = np.delete(self.position, -1, axis=0)
        else:
            self.has_food = False

    def change_direction(self, new_direction):
        ''' Cambia la dirección de la serpiente

        Recibe la nueva direccion y la cambia siempre que esta no se contraria a la
        actual. En caso de ser contraria no hace nada, lo mismo que si recibe un
        valor no valido.

        '''

        if new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction

    def biting_tail(self):
        head = self.position[0]

        for i in range(1, len(self.position)):
            if all(self.position[i] == head):
                print('Mordio su cola')
                return True

        return False
