from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """
    

    Args:
        skus (list): _description_

    Returns:
        int: _description_
    """

    if not isinstance(skus, str):
        return -1

    total = 0

    goods = defaultdict(int)

    for sku in skus:
        if sku not in ["A", "B", "C", "D"]:
            return -1

        goods[sku] += 1

    for item, number in goods.items():

        if item == "A":
            special, nonspecial = divmod(number, 3)
            total += special * 130
            total += nonspecial * 50

        elif item == "B":
            special, nonspecial = divmod(number, 2)
            total += special * 45
            total += nonspecial * 30

        elif item == "C":
            total += number * 20

        elif item == "D":
            total += number * 15

    return total



