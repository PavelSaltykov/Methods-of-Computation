from functools import cache

from common.math.function import Function
from common.math.segment import Segment
from task1.main import separate_roots
from task1.methods import secant_method


@cache
def _get_legendre_polynomial(n: int) -> Function:
    if n < 0:
        raise ValueError
    if n == 0:
        return Function("1")
    if n == 1:
        return Function("x")
    coefficient1 = (2 * n - 1) / n
    coefficient2 = (n - 1) / n
    return (Function(str(coefficient1)) * _get_legendre_polynomial(n - 1) * Function("x") -
            Function(str(coefficient2)) * _get_legendre_polynomial(n - 2))


def _get_nodes(legendre_polynomial: Function) -> list[float]:
    segment = Segment(-1, 1)
    segments = separate_roots(segment, 1000, legendre_polynomial)
    nodes = [secant_method(s, legendre_polynomial, accuracy=10 ** -12).approximate_solution for s in segments]
    return [float(n) for n in nodes]


def _get_coefficients(nodes: list[float], legendre_polynomial: Function) -> list[float]:
    def coefficient_formula(node: float) -> float:
        return 2 / ((1 - node ** 2) * float(polynomial_derivative(node)) ** 2)

    polynomial_derivative = legendre_polynomial.derivative()
    return [coefficient_formula(node) for node in nodes]


@cache
def get_nodes_coefficients(n: int) -> list[tuple[float, float]]:
    polynomial = _get_legendre_polynomial(n)
    nodes = _get_nodes(polynomial)
    coefficients = _get_coefficients(nodes, polynomial)
    return list(zip(nodes, coefficients))


def recalculate_node(segment: Segment, node: float) -> float:
    coefficient = (segment.right - segment.left) / 2
    return float(coefficient) * node + float(segment.right + segment.left) / 2


def recalculate_coefficient(segment: Segment, coefficient: float) -> float:
    return float(segment.right - segment.left) / 2 * coefficient
