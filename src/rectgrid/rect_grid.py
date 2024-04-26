from itertools import permutations
import sys
import time
from typing import Iterator

import pygame

from counter import RectCounter
from custom_exceptions import NonCuadraticError
from settings import Settings


class RectGrid:
    """Clase general que representa la
    cuadrícula"""

    def __init__(self) -> None:
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
        # Configurar pantalla
        self.screen = pygame.display.set_mode(
            (self.settings.width, self.settings.heigth)
        )
        pygame.display.set_caption("Rectángulos en Cuadrícula 5x5")

    def _draw_grid(self) -> None:
        """Dibuja la cuadrícula"""
        for x in range(0, self.settings.width, self.settings.cell_size):
            for y in range(0, self.settings.heigth, self.settings.cell_size):
                rect = pygame.Rect(
                    x, y, self.settings.cell_size, self.settings.cell_size
                )
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
            x * self.settings.cell_size,
            y * self.settings.cell_size,
            w * self.settings.cell_size,
            h * self.settings.cell_size,
        )
        pygame.draw.rect(self.screen, self.settings.blue, rect)

    def _get_rectangles(
        self, grid: tuple[int, int] = (5, 5)
    ) -> Iterator[tuple[int, int]]:
        """Devuelve una lista de tuplas con las dimensiones de todos
        los rectangulos
        posibles en una cuadrícula del tamaño grid

        Parameters
        ----------
        grid : tuple[int], optional
            _description_, by default (5, 5)

        Returns
        -------
        list[tuple[int]]
            _description_
        """
        filas, columnas = grid

        if filas != columnas:
            raise NonCuadraticError("La cuadrícula tiene que ser cuadrada")

        return permutations(range(1, filas + 1), 2)

    # Función principal
    def run(self):
        """Lanza la visualización"""
        dim_rect = self._get_rectangles()
        rect_x, rect_y = 0, 0  # Posiciones iniciales del rectángulo
        rect_w, rect_h = next(
            dim_rect
        )  # Ancho y alto del rectángulo (modificar según sea necesario)

        print(f"Dimensión inicial: ({rect_h}, {rect_w})")

        moving_right = True
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            self.screen.fill(self.settings.white)
            self._draw_grid()
            self._draw_rectangle(rect_x, rect_y, rect_w, rect_h)

            # Mover el rectángulo
            if moving_right:
                if rect_x < self.settings.grid_size - rect_w:
                    rect_x += 1
                    self.counter.add()
                else:
                    if rect_y < self.settings.grid_size - rect_h:
                        rect_x = 0
                        rect_y += 1
                        self.counter.add()
                    else:
                        moving_right = False
            else:
                try:
                    rect_w, rect_h = next(dim_rect)
                    rect_x, rect_y = 0, 0
                    moving_right = True
                except StopIteration:
                    running = False  # Detener el programa para este ejemplo
                else:
                    print(f"Dimensión siguiente: ({rect_h}, {rect_w})")

            pygame.display.flip()
            self.clock.tick(self.settings.fps)
            time.sleep(0.3)


if __name__ == "__main__":
    grid = RectGrid()
    grid.run()
    print("Rectángulos totales:", grid.counter.count)
