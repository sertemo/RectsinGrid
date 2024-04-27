"""Módulo con funciones auxiliares"""

import argparse
from typing import Any


def check_size_speed(value: Any) -> int:
    """Chequea que el argumento pasado
    esté entre 2 y 10

    Parameters
    ----------
    value : Any
        _description_

    Returns
    -------
    int
        _description_

    Raises
    ------
    argparse.ArgumentTypeError
        _description_
    """
    ivalue = int(value)
    if ivalue <= 1 or ivalue > 10:
        raise argparse.ArgumentTypeError(
            f"{value} es un valor inválido. Debe estar entre 2 y 10."
        )
    return ivalue


def transform_speed_to_delay(x: int) -> float:
    """Transforma la velocidad a un delay
    min: 2 max: 10
    min: 0.5 max: 0.01

    Parameters
    ----------
    x : int
        La velocidad

    Returns
    -------
    float
        Devuelve el delay
    """
    return -0.06125 * x + 0.6225
