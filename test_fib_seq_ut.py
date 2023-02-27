import unittest
from fib_seq import fib_seq_item


class TestFib_seq_item(unittest.TestCase):
    def test_fib_seq_item(self):
        self.assertEqual(fib_seq_item(0), [0])
        self.assertEqual(fib_seq_item(1), [0, 1])
        self.assertEqual(
            fib_seq_item(19),
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
        )
        self.assertEqual(fib_seq_item(-5), [])

        with self.assertRaises(TypeError):
            fib_seq_item(1.8)


if __name__ == "__main__":
    unittest.main()
