import unittest

from checkout_solution import checkout, ITEM_PRICES

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
        self.assertEqual(checkout("BB"), 45)
        self.assertEqual(checkout("B"), 30)
        self.assertEqual(checkout("BBB"), 45 + 30)

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
        self.assertEqual(checkout("A"), ITEM_PRICES["A"])
        self.assertEqual(checkout("B"), ITEM_PRICES["B"])
        self.assertEqual(checkout("C"), ITEM_PRICES["C"])
        self.assertEqual(checkout("D"), ITEM_PRICES["D"])
        self.assertEqual(checkout("E"), ITEM_PRICES["E"])
        self.assertEqual(checkout("F"), ITEM_PRICES["F"])
        self.assertEqual(checkout("G"), ITEM_PRICES["G"])
        self.assertEqual(checkout("H"), ITEM_PRICES["H"])
        self.assertEqual(checkout("I"), ITEM_PRICES["I"])
        self.assertEqual(checkout("J"), ITEM_PRICES["J"])
        self.assertEqual(checkout("K"), ITEM_PRICES["K"])
        self.assertEqual(checkout("L"), ITEM_PRICES["L"])
        self.assertEqual(checkout("M"), ITEM_PRICES["M"])
        self.assertEqual(checkout("N"), ITEM_PRICES["N"])
        self.assertEqual(checkout("O"), ITEM_PRICES["O"])
        self.assertEqual(checkout("P"), ITEM_PRICES["P"])
        self.assertEqual(checkout("Q"), ITEM_PRICES["Q"])
        self.assertEqual(checkout("R"), ITEM_PRICES["R"])
        self.assertEqual(checkout("S"), ITEM_PRICES["S"])
        self.assertEqual(checkout("T"), ITEM_PRICES["T"])
        self.assertEqual(checkout("U"), ITEM_PRICES["U"])
        self.assertEqual(checkout("V"), ITEM_PRICES["V"])
        self.assertEqual(checkout("W"), ITEM_PRICES["W"])
        self.assertEqual(checkout("X"), ITEM_PRICES["X"])
        self.assertEqual(checkout("Y"), ITEM_PRICES["Y"])
        self.assertEqual(checkout("Z"), ITEM_PRICES["Z"])

if __name__ == "__main__":
    unittest.main()




