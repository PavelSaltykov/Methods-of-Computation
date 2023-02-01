from decimal import Decimal

from common.math.function import Function
from common.math.segment import Segment


def left_rectangle(func: Function, segment: Segment) -> Decimal:
    return segment.length * func(segment.left)


def right_rectangle(func: Function, segment: Segment) -> Decimal:
    return segment.length * func(segment.right)


def middle_rectangle(func: Function, segment: Segment) -> Decimal:
    return segment.length * func(segment.center)


def trapeze(func: Function, segment: Segment) -> Decimal:
    return segment.length / 2 * (func(segment.left) + func(segment.right))


def simpson(func: Function, segment: Segment) -> Decimal:
    a, b = segment
    return segment.length / 6 * (func(a) + 4 * func((a + b) / 2) + func(b))


def three_eighths(func: Function, segment: Segment) -> Decimal:
    a, b = segment
    h = segment.length / 3
    return segment.length * (
            Decimal(1 / 8) * func(a) +
            Decimal(3 / 8) * func(a + h) +
            Decimal(3 / 8) * func(a + 2 * h) +
            Decimal(1 / 8) * func(b))
