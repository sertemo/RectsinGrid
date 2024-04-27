"""Módulo entry point de la aplicación"""

import argparse
import time

from rectgrid.colors import Color
from rectgrid.rect_grid import RectGrid
from rectgrid.utils import check_size


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Visualización de rectángulos en cuadrícula configurable."
    )
    parser.add_argument(
        "--size",
        type=check_size,
        default=5,
        help="Tamaño de la cuadrícula (nxn). Valores válidos entre 2 y 10.",
    )
    parser.add_argument(
        "--color",
        type=Color.from_string,
        default="azul",
        help="Color de visualización de los rectángulos (azul, verde, rojo, negro, naranja). Por defecto azul.",
    )
    args = parser.parse_args()

    if args.color == Color.AZUL:
        color = Color.AZUL.value
    elif args.color == Color.ROJO:
        color = Color.ROJO.value
    elif args.color == Color.VERDE:
        color = Color.VERDE.value
    elif args.color == Color.NEGRO:
        color = Color.NEGRO.value
    elif args.color == Color.NARANJA:
        color = Color.NARANJA.value

    print(args.color)
    rectgrid = RectGrid(grid=(args.size, args.size), color=color)
    rectgrid.run()
    print(
        f"Rectángulos totales en cuadrícula {args.size}x{args.size}:",
        rectgrid.counter.count,
    )
    time.sleep(3)


if __name__ == "__main__":
    main()
