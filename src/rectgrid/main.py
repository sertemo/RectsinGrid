import argparse
import time
from typing import Any

from rectgrid.rect_grid import RectGrid


def main() -> None:
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
        if ivalue < 1 or ivalue > 10:
            raise argparse.ArgumentTypeError(
                f"{value} es un valor inválido para el tamaño de la cuadrícula. Debe estar entre 1 y 10."
            )
        return ivalue

    parser = argparse.ArgumentParser(
        description="Visualización de rectángulos en cuadrícula configurable."
    )
    parser.add_argument(
        "--size",
        type=check_size,
        default=5,
        help="Tamaño de la cuadrícula (nxn). Valores válidos entre 1 y 10.",
    )
    args = parser.parse_args()

    print(args.size)

    rectgrid = RectGrid((args.size, args.size))
    rectgrid.run()
    print("Rectángulos totales:", rectgrid.counter.count)
    time.sleep(3)


if __name__ == "__main__":
    main()
