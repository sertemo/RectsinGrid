import pytest

from rectgrid.colors import Color


def test_good_color() -> None:
    s = 'verDE'
    assert isinstance(Color.from_string(s), Color)

def test_bad_color() -> None:
    s = 'escarlata'
    with pytest.raises(ValueError):
        Color.from_string(s)
