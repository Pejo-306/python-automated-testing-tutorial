import pytest

from random_utils.utils import *


BLACK_MAGIC = "???"


@pytest.mark.parametrize('test_input,expected', [
    (5, 25),
    (-3, 9),
    (0, 0)
])
def test_square(test_input: int, expected: int):
    assert square(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    (5, 125),
    (-3, -27),
    (0, 0)
])
def test_cube(test_input: int, expected: int):
    assert cube(test_input) == expected


@pytest.mark.xfail
def test_divide_by_zero():
    assert divide_by_zero() == BLACK_MAGIC


def test_throw_exception():
    with pytest.raises(Exception):
        throw_exception()


@pytest.mark.parametrize('test_input,expected', [
    ('Pesho', 'Hello Pesho!\n'),
    ('Gosho', 'Hello Gosho!\n')
])
def test_print_hello(test_input, expected, capture_stdout):
    print_hello(test_input)
    assert capture_stdout['stdout'] == expected
