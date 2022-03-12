import unittest

from checkout_solution import checkout, item_prices

class TestCheckout(unittest.TestCase):

    @unittest.skip("Not testing this round right now")
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

    @unittest.skip("Not testing this round right now")
    def test_round_2(self):
        self.assertEqual(checkout("BBEE"), 40 * 2 + 30)
        self.assertEqual(checkout("BBBEE"), 40 * 2 + 45)
        self.assertEqual(checkout("BBBE"), 45 + 30 + 40)
        self.assertEqual(checkout("CAABAAB"), 20 + 130 + 50 + 45)
        self.assertEqual(checkout("A" * 5), 200)
        self.assertEqual(checkout("A" * 8), 200 + 130)
        self.assertEqual(checkout("A" * 9), 200 + 130 + 50)
        self.assertEqual(checkout("WOOF"), -1)
        self.assertEqual(checkout(525), -1)
        self.assertEqual(checkout("525"), -1)
        self.assertEqual(checkout(["A", "A", "B"]), -1)
        self.assertEqual(checkout("E" * 5), 40 * 5)

    def test_round_3(self):
        # self.assertEqual(checkout("F" * 3), 20)
        # self.assertEqual(checkout("F" * 4), 30)
        # self.assertEqual(checkout("F" * 2), 20)
        self.assertEqual(checkout("BBEE"), 40 * 2 + 30)
        self.assertEqual(checkout("BBBEE"), 40 * 2 + 45)
        self.assertEqual(checkout("BBBE"), 45 + 30 + 40)
        self.assertEqual(checkout("CAABAAB"), 20 + 130 + 50 + 45)
        self.assertEqual(checkout("A" * 5), 200)
        self.assertEqual(checkout("A" * 8), 200 + 130)
        self.assertEqual(checkout("A" * 9), 200 + 130 + 50)
        self.assertEqual(checkout(525), -1)
        self.assertEqual(checkout("525"), -1)
        self.assertEqual(checkout(["A", "A", "B"]), -1)
        self.assertEqual(checkout("E" * 5), 40 * 5)
        self.assertEqual(checkout("A"), item_prices["A"])
        self.assertEqual(checkout("B"), item_prices["B"])
        self.assertEqual(checkout("C"), item_prices["C"])
        self.assertEqual(checkout("D"), item_prices["D"])
        self.assertEqual(checkout("E"), item_prices["E"])
        self.assertEqual(checkout("F"), item_prices["F"])
        self.assertEqual(checkout("G"), item_prices["G"])
        self.assertEqual(checkout("H"), item_prices["H"])
        self.assertEqual(checkout("I"), item_prices["I"])
        self.assertEqual(checkout("J"), item_prices["J"])
        self.assertEqual(checkout("K"), item_prices["K"])
        self.assertEqual(checkout("L"), item_prices["L"])
        self.assertEqual(checkout("M"), item_prices["M"])
        self.assertEqual(checkout("N"), item_prices["N"])
        self.assertEqual(checkout("O"), item_prices["O"])
        self.assertEqual(checkout("P"), item_prices["P"])
        self.assertEqual(checkout("Q"), item_prices["Q"])
        self.assertEqual(checkout("R"), item_prices["R"])
        self.assertEqual(checkout("S"), item_prices["S"])
        self.assertEqual(checkout("T"), item_prices["T"])
        self.assertEqual(checkout("U"), item_prices["U"])
        self.assertEqual(checkout("V"), item_prices["V"])
        self.assertEqual(checkout("W"), item_prices["W"])
        self.assertEqual(checkout("X"), item_prices["X"])
        self.assertEqual(checkout("Y"), item_prices["Y"])
        self.assertEqual(checkout("Z"), item_prices["Z"])

if __name__ == "__main__":
    unittest.main()


