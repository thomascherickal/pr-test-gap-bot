"""Basic cart pricing."""


def subtotal(prices: list[float]) -> float:
    """Sum of item prices, rounded to cents."""
    return round(sum(prices), 2)
