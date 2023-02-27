import unittest
from fib_rec import fib_rec_item, fib_rec


class TestFib_rec(unittest.TestCase):
    def test_fib_rec_item(self):
        self.assertEqual(fib_rec_item(0), 0)
        self.assertEqual(fib_rec_item(1), 1)
        self.assertEqual(fib_rec_item(19), 4181)

        with self.assertRaises(RecursionError):
            fib_rec_item(1.8)

        with self.assertRaises(RecursionError):
            fib_rec_item(-5)


if __name__ == "__main__":
    unittest.main()
