# noinspection PyShadowingBuiltins,PyUnusedLocal


def compute(x: int, y: int) -> int:
    """
    Sum the two input numbers, which must both be between 0-100.

    Args:
        x (int): the first number to sum
        y (int): the second number to sum

    Raises:
        ValueError: if x or y are not between 0-100

    Returns:
        int: a positive integer between 0-200
    """
    if (x < 0) or (x > 100) or (y < 0) or (y > 100):
        raise ValueError("x and y should be between 0-100")

    result = x + y

    return result
