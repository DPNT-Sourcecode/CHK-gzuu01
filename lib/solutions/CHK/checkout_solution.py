from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string

ITEM_PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50
}

SPECIALS = ["A", "B", "E", "F", "H", "K", "N", "P", "Q", "R", "U", "V"]

DISCOUNTED_BY_OTHERS = ["B", "M", "Q"]


def checkout(skus: str) -> int:
    """
    Return the total price of a string sequence of skus.

    Args:
        skus (str): a sequence of skus e.g. "ABBA"

    Returns:
        int: the total cost of these skus, including special offers
    """

    if not isinstance(skus, str):
        return -1

    total = 0

    goods = defaultdict(int)

    b_potentially_free = 0
    m_potentially_free = 0
    q_potentially_free = 0

    for sku in skus:
        if sku not in ITEM_PRICES:
            return -1

        goods[sku] += 1

    for item, number in goods.items():

        # If the item is discounted by others, we do the calc at the end
        if item in DISCOUNTED_BY_OTHERS:
            continue

        # If the item doesn't have a special on itself
        if item not in SPECIALS:
            total += number * ITEM_PRICES[item]

        if item == "A":
            special_5, remainder = divmod(number, 5)
            special_3, nonspecial = divmod(remainder, 3)
            total += special_5 * 200
            total += special_3 * 130
            total += nonspecial * ITEM_PRICES[item]

        elif item == "E":
            total += number * ITEM_PRICES[item]
            b_potentially_free, _ = divmod(number, 2)

        elif item == "F":
            special, nonspecial = divmod(number, 3)
            total += special * 2 * ITEM_PRICES[item]
            total += nonspecial * ITEM_PRICES[item]

        elif item == "H":
            special_10, remainder = divmod(number, 10)
            special_5, nonspecial = divmod(remainder, 5)
            total += special_10 * 80
            total += special_5 * 45
            total += nonspecial * ITEM_PRICES[item]

        elif item == "K":
            special, nonspecial = divmod(number, 2)
            total += special * 150
            total += nonspecial * ITEM_PRICES[item]

        elif item == "N":
            total +=  number * ITEM_PRICES[item]
            m_potentially_free, _ = divmod(number, 3)

        elif item == "P":
            special, nonspecial = divmod(number, 5)
            total += special * 200
            total += nonspecial * ITEM_PRICES[item]

        elif item == "R":
            total += number * ITEM_PRICES[item]
            q_potentially_free, _ = divmod(number, 3)   

        elif item == "U":
            special, nonspecial = divmod(number, 4)
            total += special * 3 * ITEM_PRICES[item]
            total += nonspecial * ITEM_PRICES[item]

        elif item == "V":
            special_3, remainder = divmod(number, 3)
            special_2, nonspecial = divmod(remainder, 2)
            total += special_3 * 130
            total += special_2 * 90
            total += nonspecial * ITEM_PRICES[item]   

    # B
    b_total_free = min(goods["B"], b_potentially_free)
    goods["B"] -= b_total_free
    b_special, b_nonspecial = divmod(goods["B"], 2)
    total += b_special * 45
    total += b_nonspecial * ITEM_PRICES["B"]

    # M
    m_total_free = min(goods["M"], m_potentially_free)
    goods["M"] -= m_total_free
    total += goods["M"] * ITEM_PRICES["M"]

    # Q
    q_total_free = min(goods["Q"], q_potentially_free)
    goods["Q"] -= q_total_free
    q_special, q_nonspecial = divmod(goods["Q"], 3)
    total += q_special * 80
    total += q_nonspecial * ITEM_PRICES["Q"]

    return total
    