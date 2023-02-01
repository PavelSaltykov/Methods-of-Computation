from decimal import Decimal
from functools import reduce
from typing import Tuple


def lagrange_interpolation(x: Decimal, table: list[Tuple[Decimal, Decimal]]) -> Decimal:
    def get_differences(x_: Decimal, points_: list[Decimal], ignored_index: int):
        return [x_ - x_i for index_, x_i in enumerate(points_) if index_ != ignored_index]

    points = [row[0] for row in table]

    result = Decimal(0)
    for index, (point, value) in enumerate(table):
        result += (reduce(lambda a, b: a * b, get_differences(x, points, index), Decimal(1)) /
                   reduce(lambda a, b: a * b, get_differences(point, points, index), Decimal(1))) * value

    return result


def newton_interpolation(x: Decimal, table: list[Tuple[Decimal, Decimal]]) -> Decimal:
    def get_divided_differences() -> list[Decimal]:
        points_ = [row[0] for row in table]
        values_ = [row[1] for row in table]

        differences: list[list[Decimal]] = [[values_[0]]]
        for diff_order in range(1, len(table)):
            current_order_differences = []
            current_points = list(zip(points_[:-diff_order], points_[diff_order:]))

            if diff_order == 1:
                current_values = list(zip(values_[:-1], values_[1:]))
            else:
                current_values = list(zip(differences[diff_order - 1][:-1], differences[diff_order - 1][1:]))

            z = list(zip(current_points, current_values))
            for two_points, two_values in z:
                current_order_differences.append((two_values[1] - two_values[0]) / (two_points[1] - two_points[0]))

            differences.append(current_order_differences)

        return [d[0] for d in differences]

    points = [row[0] for row in table]

    result = Decimal(0)
    current_multiplier = Decimal(1)
    for index, difference in enumerate(get_divided_differences()):
        result += difference * current_multiplier
        current_multiplier *= x - points[index]
    return result
