# -*- coding: utf-8 -*-

import sys
import time
import pygame

import stage
import snake


def main():
    pygame.init()

    width, height = 900, 600
    background = 0x0f, 0x0f, 0x0f

    cells_x, cells_y = 45, 30

    screen = pygame.display.set_mode((width, height))

    cells_width = width / cells_x
    cells_height = height / cells_y

    game_stage = stage.Stage(cells_x, cells_y)
    player = snake.Snake(int(cells_x / 2), int(cells_y / 2))

    game_over = False

    while not game_over:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)

                if key_name == 'up' or key_name == 'w':
                    player.change_direction('up')
                elif key_name == 'down' or key_name == 's':
                    player.change_direction('down')
                elif key_name == 'left' or key_name == 'a':
                    player.change_direction('left')
                elif key_name == 'right' or key_name == 'd':
                    player.change_direction('right')

        game_over = game_stage.update_state(player)

        screen.fill(background)

        for y in range(cells_y):
            for x in range(cells_x):
                poly = [(x * cells_width, y * cells_height),
                        ((x + 1) * cells_width, y * cells_height),
                        ((x + 1) * cells_width, (y + 1) * cells_height),
                        (x * cells_width, (y + 1) * cells_height)]

                if game_stage.get_cell(x, y) == 3:
                    pygame.draw.polygon(screen, (0x1f, 0x1f, 0x1f), poly)
                elif game_stage.get_cell(x, y) == 2:
                    pygame.draw.polygon(screen, (0xfc, 0x90, 0x03), poly)
                elif game_stage.get_cell(x, y) == 1:
                    pygame.draw.polygon(screen, (0x18, 0xa8, 0x2b), poly)
                else:
                    pygame.draw.lines(
                        screen, (0x1f, 0x1f, 0x1f), True, poly, 1)

        pygame.display.flip()
        time.sleep(0.2/game_stage.get_speed())


if __name__ == '__main__':
    main()
