from decimal import Decimal


def calculate_first_derivatives(f_values: list[Decimal], step: Decimal) -> list[Decimal]:
    if len(f_values) < 3:
        raise ValueError("At least three function values are required")

    derivative_first_point = (-3 * f_values[0] + 4 * f_values[1] - f_values[2]) / (2 * step)

    calculating_values = list(zip(f_values[:-2], f_values[2:]))
    central_derivatives = [(right - left) / (2 * step) for left, right in calculating_values]

    derivative_last_point = (3 * f_values[-1] - 4 * f_values[-2] + f_values[-3]) / (2 * step)
    return [derivative_first_point, *central_derivatives, derivative_last_point]


def calculate_second_derivatives(f_values: list[Decimal], step: Decimal) -> list[Decimal]:
    if len(f_values) < 3:
        raise ValueError("At least three function values are required")

    calculating_values = list(zip(f_values[:-2], f_values[1:-1], f_values[2:]))
    central_derivatives = [(right - 2 * mid + left) / (step ** 2) for left, mid, right in calculating_values]
    return [None, *central_derivatives, None]
