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
            b_special, b_nonspecial = divmod(number, 2)
            # total += special * 45
            # total += nonspecial * 30

        elif item == "C":
            total += number * 20

        elif item == "D":
            total += number * 15

        elif item == "E":
            total += number * 40
            b_potentially_free, _ = divmod(number, 2)

    # Now handle the free Bs
    b_total_free = max(goods["B"], b_potentially_free)
    b_special_free = max(b_special, b_total_free)
    b_nonspecial_free = max(b_total_free - b_special_free, 0)

    b_nonspecial -= b_nonspecial_free
    b_special -= b_special_free

    total += b_special * 45
    total += b_nonspecial * 30

    return total

