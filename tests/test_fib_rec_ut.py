import unittest

from fibonacci.fib_rec import fib_rec_item, fib_rec


class TestFib_rec(unittest.TestCase):
    def test_fib_rec_item(self):
        self.assertEqual(fib_rec_item(0), 0)
        self.assertEqual(fib_rec_item(1), 1)
        self.assertEqual(fib_rec_item(19), 4181)

        with self.assertRaises(RecursionError):
            fib_rec_item(1.8)

        with self.assertRaises(RecursionError):
            fib_rec_item(-5)

    def test_fib_rec(self):
        self.assertEqual(fib_rec(0), [0])
        self.assertEqual(fib_rec(1), [0, 1])
        self.assertEqual(
            fib_rec(19),
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
        self.assertEqual(fib_rec(-5), [])

        with self.assertRaises(TypeError):
            fib_rec(1.8)


if __name__ == "__main__":
    unittest.main()
