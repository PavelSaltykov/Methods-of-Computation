from decimal import Decimal


def method_runge(integral_value_m: Decimal, integral_value_ml, coefficient_l: int, d: int) -> Decimal:
    r = d + 1
    return (coefficient_l ** r * integral_value_ml - integral_value_m) / (coefficient_l ** r - 1)
