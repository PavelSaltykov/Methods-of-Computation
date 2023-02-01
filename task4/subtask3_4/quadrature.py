from decimal import Decimal
from functools import cache

from common.math.function import Function
from common.math.segment import Segment


@cache
def get_h(segment: Segment, m: int) -> Decimal:
    return (segment.right - segment.left) / m


@cache
def _get_points(segment: Segment, m: int) -> list[Decimal]:
    return segment.equidistant_points(m)


@cache
def _sum_of_inner_values(func: Function, segment: Segment, m: int) -> Decimal:
    points = _get_points(segment, m)[1:-1]
    values = [func(p) for p in points]
    return sum(values)


@cache
def _sum_of_boundary_values(func: Function, segment: Segment) -> Decimal:
    return func(segment.left) + func(segment.right)


@cache
def _sum_of_middle_values(func: Function, segment: Segment, m: int) -> Decimal:
    points = _get_points(segment, m)[:-1]
    h = get_h(segment, m)
    middles = [p + h / 2 for p in points]
    values = [func(p) for p in middles]
    return sum(values)


def calculate_error(const: Decimal, func: Function, segment: Segment, d: int, h: Decimal) -> Decimal:
    m = abs(func.derivative(d + 1)).max(segment)
    a, b = segment
    return const * m * (b - a) * h ** (d + 1)


def left_rectangles(func: Function, segment: Segment, m: int) -> tuple[Decimal, Decimal]:
    h = get_h(segment, m)
    f_0 = func(segment.left)
    w = _sum_of_inner_values(func, segment, m)
    result = h * (f_0 + w)

    const, d = Decimal(1 / 2), 0
    error = calculate_error(const, func, segment, d, h)
    return result, error


def right_rectangles(func: Function, segment: Segment, m: int) -> tuple[Decimal, Decimal]:
    h = get_h(segment, m)
    f_m = func(segment.right)
    w = _sum_of_inner_values(func, segment, m)
    result = h * (w + f_m)

    const, d = Decimal(1 / 2), 0
    error = calculate_error(const, func, segment, d, h)
    return result, error


def middle_rectangles(func: Function, segment: Segment, m: int) -> tuple[Decimal, Decimal]:
    h = get_h(segment, m)
    q = _sum_of_middle_values(func, segment, m)
    result = h * q

    const, d = Decimal(1 / 24), 1
    error = calculate_error(const, func, segment, d, h)
    return result, error


def trapezes(func: Function, segment: Segment, m: int) -> tuple[Decimal, Decimal]:
    h = get_h(segment, m)
    z = _sum_of_boundary_values(func, segment)
    w = _sum_of_inner_values(func, segment, m)
    result = h / 2 * (z + 2 * w)

    const, d = Decimal(1 / 12), 1
    error = calculate_error(const, func, segment, d, h)
    return result, error


def simpson(func: Function, segment: Segment, m: int) -> tuple[Decimal, Decimal]:
    h = get_h(segment, m)
    z = _sum_of_boundary_values(func, segment)
    w = _sum_of_inner_values(func, segment, m)
    q = _sum_of_middle_values(func, segment, m)
    result = h / 6 * (z + 2 * w + 4 * q)

    const, d = Decimal(1 / 2880), 3
    error = calculate_error(const, func, segment, d, h)
    return result, error
