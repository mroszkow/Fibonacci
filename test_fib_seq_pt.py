import pytest
from fib_seq import feb_seq_item


@pytest.mark.parametrize(
    "input_number, result",
    [
        (0, [0]),
        (1, [0, 1]),
        (
            19,
            [
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
            ],
        ),
        (-5, []),
    ],
)
def test_fib_seq_item(input_number, result):
    assert feb_seq_item(input_number) == result


def test_fib_seq_item_float_input():
    with pytest.raises(TypeError):
        feb_seq_item(1.8)
