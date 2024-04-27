"""Módulo con los colores posibles"""

from enum import Enum


class Color(Enum):
    AZUL = (0, 0, 255)
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)
    NARANJA = (255, 128, 0)

    @staticmethod
    def from_string(s):
        try:
            return Color[s.upper()]
        except KeyError:
            raise ValueError(
                f"Color no válido: {s}. Los colores válidos son: azul, rojo, verde, naranja y negro."
            )
