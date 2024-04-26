import pytest

from rectgrid.rect_grid import RectGrid
from rectgrid.custom_exceptions import NonCuadraticError

def test_bad_grid_shape() -> None:
    with pytest.raises(NonCuadraticError):
        grid = RectGrid((4, 5))

def test_bad_value() -> None:
    with pytest.raises(ValueError):
        grid = RectGrid(67)

def test_bad_object_type() -> None:
    with pytest.raises(ValueError):
        grid = RectGrid([8, 8])