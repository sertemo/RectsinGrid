"""Módulo con funciones auxiliares"""

import argparse
from typing import Any


def check_size(value: Any) -> int:
    """Chequea que el argumento pasado
    esté entre 1 y 10

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
            f"{value} es un valor inválido para el tamaño de la cuadrícula. Debe estar entre 2 y 10."
        )
    return ivalue
