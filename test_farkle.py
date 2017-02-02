import unittest
from farkle import Die

class TestFarkle(unittest.TestCase):
    def test_die_init(self):
        die1 = Die(1)
        self.assertEqual(die1.number, 1)
        self.assertEqual(die1.sides, 6)


if __name__ == '__main__':
    unittest.main()
