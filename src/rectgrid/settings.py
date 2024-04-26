"""Módulo con los settings y constantes"""


class Settings:
    def __init__(self) -> None:
        self.width = 500
        self.heigth = 500
        self.grid_size = 5
        self.cell_size = self.width // self.grid_size
        self.fps = 60

        # Colores
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = (0, 0, 255)
