from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
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

    item_prices = {
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

    for sku in skus:
        if sku not in item_prices:
            return -1

        goods[sku] += 1

    for item, number in goods.items():

        if item == "A":
            special_5, remainder = divmod(number, 5)
            special_3, nonspecial = divmod(remainder, 3)
            total += special_5 * 200
            total += special_3 * 130
            total += nonspecial * item_prices[item]

        elif item == "B":
            continue

        elif item == "C":
            total += number * item_prices[item]

        elif item == "D":
            total += number * item_prices[item]

        elif item == "E":
            total += number * item_prices[item]
            b_potentially_free, _ = divmod(number, 2)

        elif item == "F":
            special, nonspecial = divmod(number, 3)
            total += special * 20
            total += nonspecial * item_prices[item]

    # Revisit B now we know the total of Bs and Es
    b_total_free = min(goods["B"], b_potentially_free)
    goods["B"] -= b_total_free
    b_special, b_nonspecial = divmod(goods["B"], 2)

    total += b_special * 45
    total += b_nonspecial * 30

    return total



