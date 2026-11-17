"""Shipping cost rules (the demo PR adds this file with NO tests)."""


def shipping_cost(weight_kg: float, country: str, express: bool = False) -> float:
    if weight_kg <= 0:
        raise ValueError("weight must be positive")

    if country == "IN":
        base = 40.0 if weight_kg <= 2 else 40.0 + (weight_kg - 2) * 15.0
    elif country in ("US", "CA"):
        base = 120.0 if weight_kg <= 1 else 120.0 + (weight_kg - 1) * 60.0
    else:
        base = 250.0 + weight_kg * 90.0

    if express:
        base *= 1.5

    return round(base, 2)
