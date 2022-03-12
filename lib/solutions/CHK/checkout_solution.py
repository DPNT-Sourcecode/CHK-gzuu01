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

    for sku in skus:
        if sku not in ["A", "B", "C", "D", "E"]:
            return -1

        goods[sku] += 1

    for item, number in goods.items():

        if item == "A":
            special_5, remainder = divmod(number, 5)
            special_3, nonspecial = divmod(remainder, 3)
            total += special_5 * 200
            total += special_3 * 130
            total += nonspecial * 50

        elif item == "B":
            continue

        elif item == "C":
            total += number * 20

        elif item == "D":
            total += number * 15

        elif item == "E":
            total += number * 40
            b_potentially_free, _ = divmod(number, 2)

        elif item == "F":
            special, nonspecial = divmod(number, 3)
            total += special * 20
            total += nonspecial * 10

    # Revisit B now we know the total of Bs and Es
    b_total_free = min(goods["B"], b_potentially_free)
    goods["B"] -= b_total_free
    b_special, b_nonspecial = divmod(goods["B"], 2)

    total += b_special * 45
    total += b_nonspecial * 30

    return total

