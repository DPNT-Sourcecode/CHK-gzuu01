import unittest

from checkout_solution import checkout

class TestCheckout(unittest.TestCase):

    @unittest.skip("Running tests for r2 now")
    def test_round_1(self):
        self.assertEqual(
            checkout("ABCDABCDABCDA"),
            130 + 50 + 45 + 30 + 20 * 3 + 15 * 3
        )
        self.assertEqual(checkout("CAABAAAAB"), 20 + 130 * 2 + 45)
        self.assertEqual(checkout("WOOF"), -1)
        self.assertEqual(checkout(525), -1)
        self.assertEqual(checkout("525"), -1)
        self.assertEqual(checkout(["A", "A", "B"]), -1)

    def test_round_2(self):
        self.assertEqual(checkout("BBEE"), 40 * 2 + 30)

if __name__ == "__main__":
    unittest.main()

