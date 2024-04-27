import argparse

import pytest

from rectgrid.utils import transform_speed_to_delay, check_size_speed

def good_conversion_min() -> None:
    speed = 2
    assert transform_speed_to_delay(speed) == 0.5

def good_conversion_max() -> None:
    speed = 10
    assert transform_speed_to_delay(speed) == 0.01

def bad_conversion() -> None:
    speed = 5
    assert transform_speed_to_delay(speed) != 0.01

def good_size_speed() -> None:
    value = 5
    assert check_size_speed(value) == value

def bad_type_size_speed() -> None:
    value = 'juan'
    with pytest.raises(argparse.ArgumentTypeError):
        check_size_speed(value)

def out_of_max_bounds_size_speed() -> None:
    value = 15
    with pytest.raises(argparse.ArgumentTypeError):
        check_size_speed(value)

def out_of_min_bounds_size_speed() -> None:
    value = 1
    with pytest.raises(argparse.ArgumentTypeError):
        check_size_speed(value)

def zero_value_bounds_size_speed() -> None:
    value = 0
    with pytest.raises(argparse.ArgumentTypeError):
        check_size_speed(value)