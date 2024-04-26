from itertools import permutations
import sys
import time
from typing import Iterator

import pygame

from rectgrid.counter import RectCounter
from rectgrid.custom_exceptions import NonCuadraticError
from rectgrid.settings import Settings


class RectGrid:
    """Clase general que representa la
    cuadrícula"""

    # TODO hacer que el tamaño sea un parámetro de entrada
    def __init__(self, grid: tuple[int, int] = (5, 5)) -> None:
        """Inicializa la visualización

        Returns
        -------
        _type_
            _description_

        Raises
        ------
        NonCuadraticError
            Si pasas una cuadrícula no cuadrada
        """
        # Inicializar Pygame
        pygame.init()
        self.clock = pygame.time.Clock()
        # Settings
        self.settings = Settings()
        # Contador para contar número de rectángulos
        self.counter = RectCounter()
        self.grid = self._validate_cuadratic(grid)
        self.grid_size = self.grid[0]
        self.width = self.settings.default_scale * self.grid_size
        self.height = self.width
        self.cell_size = self.width // self.grid_size

        # Configurar pantalla
        self.screen = pygame.display.set_mode((self.width, self.height))
        # Título
        pygame.display.set_caption(
            f"Rectángulos en Cuadrícula {self.grid[0]}x{self.grid[1]}"
        )
        # Validamos grid

    def _validate_cuadratic(self, grid: tuple[int, int]) -> tuple[int, int]:
        """Valida que la grid sea cuadrada

        Parameters
        ----------
        grid : tuple[int, int]
            _description_

        Returns
        -------
        tuple[int, int]
            devuelve la grid en caso de pasar las validaciones
        """
        if not isinstance(grid, tuple):
            raise ValueError("Tienes que pasar una tupla")
        if len(grid) != 2:
            raise ValueError("La cuadrícula tiene que ser de 2 dimensiones")
        if grid[0] != grid[1]:
            raise NonCuadraticError("La cuadrícula tiene que ser cuadrada")

        return grid

    def _draw_grid(self) -> None:
        """Dibuja la cuadrícula"""
        for x in range(0, self.width, self.cell_size):
            for y in range(0, self.height, self.cell_size):
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, self.settings.black, rect, 1)

    def _draw_rectangle(self, x: int, y: int, w: int, h: int) -> None:
        """Dibuja un rectángulo

        Parameters
        ----------
        x : int
            posición del cuadrado sup izq en x
        y : int
            posición del cuadrado sup izq en y
        w : int
            número de columnas que ocupa
        h : int
            número de filas que ocupa
        """
        rect = pygame.Rect(
            x * self.cell_size,
            y * self.cell_size,
            w * self.cell_size,
            h * self.cell_size,
        )
        pygame.draw.rect(self.screen, self.settings.blue, rect)

    def _get_rectangles(self) -> Iterator[tuple[int, int]]:
        """Devuelve una lista de tuplas con las dimensiones de todos
        los rectangulos
        posibles en una cuadrícula del tamaño grid

        Returns
        -------
        Iterator[tuple[int, int]]
            Devuelve un iterador con tuplas que representan
            dimensiones del rectangulo siguiente
        """
        return permutations(range(1, self.grid[0] + 1), 2)

    # Función principal
    def run(self):
        """Lanza la visualización"""
        dim_rect = self._get_rectangles()
        rect_x, rect_y = 0, 0  # Posiciones iniciales del rectángulo
        rect_w, rect_h = next(dim_rect)

        print(f"Dimensión inicial: ({rect_h}, {rect_w})")

        moving_right = True
        running = True
        self.counter.add()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            self.screen.fill(self.settings.white)
            self._draw_grid()
            self._draw_rectangle(rect_x, rect_y, rect_w, rect_h)
            # self.counter.add()

            # Mover el rectángulo
            if moving_right:
                if rect_x < self.grid_size - rect_w:
                    rect_x += 1
                    self.counter.add()
                else:
                    if rect_y < self.grid_size - rect_h:
                        rect_x = 0
                        rect_y += 1
                        self.counter.add()
                    else:
                        moving_right = False
            else:
                try:
                    rect_w, rect_h = next(dim_rect)
                except StopIteration:
                    running = False  # Detener el programa para este ejemplo
                else:
                    print(f"Dimensión siguiente: ({rect_h}, {rect_w})")
                    rect_x, rect_y = 0, 0
                    moving_right = True
                    self.counter.add()

            pygame.display.flip()
            self.clock.tick(self.settings.fps)
            time.sleep(self.settings.delay)


if __name__ == "__main__":
    grid = RectGrid()
    grid.run()
    print("Rectángulos totales:", grid.counter.count)
