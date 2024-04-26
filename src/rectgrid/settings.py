"""Módulo con los settings y constantes"""


class Settings:
    def __init__(self) -> None:
        self.default_scale = 100
        self.fps = 60
        # Movimiento del rectángulo
        self.delay = 0.1

        # Colores
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = (0, 0, 255)
