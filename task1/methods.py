from dataclasses import dataclass
from decimal import Decimal
from typing import Callable

from common.math.function import Function
from common.math.segment import Segment
from common.utils import to_decimal


@dataclass
class MethodResult:
    initial_approximation: list[Decimal]
    number_of_step: int
    approximate_solution: Decimal
    delta: Decimal


def bisection_method(segment: Segment, f: Callable[[Decimal], Decimal], accuracy: Decimal) -> MethodResult:
    initial_approximation = segment.center

    current_segment = segment
    step = 0

    while step == 0 or current_segment.length > 2 * accuracy:
        center = current_segment.center
        if f(current_segment.left) * f(center) <= 0:
            current_segment = Segment(current_segment.left, center)
        else:
            current_segment = Segment(center, current_segment.right)
        step += 1

    approximate_solution = current_segment.center
    delta = abs(current_segment.length)
    return MethodResult([initial_approximation], step, approximate_solution, delta)


def newton_method(segment: Segment, f: Function, accuracy: Decimal) -> MethodResult:
    derivative = f.derivative()

    initial_approximation = choose_initial_approximation(segment, f)

    previous_x = segment.left
    current_x = previous_x - to_decimal(f(previous_x) / derivative(previous_x))

    step = 1
    while abs(current_x - previous_x) > accuracy:
        previous_x = current_x
        current_x = previous_x - to_decimal(f(previous_x) / derivative(previous_x))

        step += 1

    approximate_solution = current_x
    delta = abs(approximate_solution - previous_x)
    return MethodResult([initial_approximation], step, approximate_solution, delta)


def modified_newton_method(segment: Segment, f: Function, accuracy: Decimal) -> MethodResult:
    derivative = f.derivative()

    initial_approximation = choose_initial_approximation(segment, f)

    previous_x = segment.left
    current_x = previous_x - to_decimal(f(previous_x) / derivative(initial_approximation))

    step = 1
    while abs(current_x - previous_x) > accuracy:
        previous_x = current_x
        current_x = previous_x - to_decimal(f(previous_x) / derivative(initial_approximation))

        step += 1

    approximate_solution = current_x
    delta = abs(approximate_solution - previous_x)
    return MethodResult([initial_approximation], step, approximate_solution, delta)


def secant_method(segment: Segment, f: Callable[[Decimal], Decimal], accuracy: Decimal) -> MethodResult:
    initial_approximations = [segment.left, segment.right]

    previous_x = segment.left
    current_x = segment.right
    next_x = current_x - to_decimal(f(current_x) / (f(current_x) - f(previous_x))) * (current_x - previous_x)

    step = 1
    while abs(next_x - current_x) > accuracy:
        previous_x = current_x
        current_x = next_x
        next_x = current_x - to_decimal(f(current_x) / (f(current_x) - f(previous_x))) * (current_x - previous_x)

        step += 1

    approximate_solution = next_x
    delta = abs(approximate_solution - current_x)
    return MethodResult(initial_approximations, step, approximate_solution, delta)


def choose_initial_approximation(segment: Segment, f: Function, step: Decimal = 10 ** -5) -> Decimal:
    second_derivative = f.derivative(2)

    initial_approximation = segment.left
    while segment.contains(initial_approximation):
        if to_decimal(f(initial_approximation) * second_derivative(initial_approximation)) > 0:
            return initial_approximation
        initial_approximation += Decimal(step)

    return segment.right
