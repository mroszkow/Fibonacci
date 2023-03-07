import pytest

from fibonacci.fib_rec import fib_rec_item, fib_rec

@pytest.mark.parametrize("input_number,result", [
    (0, 0),
    (1, 1),
    (19, 4181),

])

def test_fib_rec_item(input_number, result):
    assert fib_rec_item(input_number) == result

def test_fib_rec_item_float_input():
    with pytest.raises(RecursionError):
        fib_rec_item(1.8)

def test_fib_rec_item_negative_input():
    with pytest.raises(RecursionError):
        fib_rec_item(-5)


@pytest.mark.parametrize("input_number,result", [
    (0, [0]),
    (1, [0, 1]),
    (-5, []),
    (19, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]),
])

def test_fib_rec(input_number, result):
    assert fib_rec(input_number) == result

def test_fib_rec_float_input():
    with pytest.raises(TypeError):
        fib_rec(1.8)