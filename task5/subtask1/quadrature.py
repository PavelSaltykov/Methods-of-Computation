from dataclasses import dataclass

import numpy as np

from common.math.function import Function
from common.math.quadrature import get_moments, get_coefficients, quadrature_formula
from common.math.segment import Segment
from task1.main import separate_roots
from task1.methods import bisection_method


@dataclass
class QuadratureResult:
    value: float
    weight_moments: list[float]
    orthogonal_polynomial: Function
    quadrature_nodes: list[float]
    quadrature_coefficients: list[float]


def _get_polynomial(moments: list[float]) -> Function:
    def get_polynomial_coefficients() -> list[float]:
        matrix = []
        for i in range(n):
            row = list(reversed(moments[i:n + i]))
            matrix.append(row)
        right_part = [-m for m in moments[n:]]
        return list(np.linalg.solve(matrix, right_part))

    n = len(moments) // 2
    coefficients = get_polynomial_coefficients()
    polynomial = Function(f"x ** {n}")
    for index, coefficient in enumerate(coefficients, 1):
        polynomial += Function(str(coefficient)) * Function(f"x ** {n - index}")
    return polynomial


def _get_nodes(segment: Segment, polynomial: Function) -> list[float]:
    segments = separate_roots(segment, n=1000, f=polynomial)
    nodes = [bisection_method(s, polynomial, accuracy=10 ** -12).approximate_solution for s in segments]
    return [float(n) for n in nodes]


def calculate_approximate_value(segment: Segment, weight: Function, func: Function, n: int) -> QuadratureResult:
    moments = get_moments(segment, weight, 2 * n)
    polynomial = _get_polynomial(moments)
    nodes = _get_nodes(segment, polynomial)
    assert len(nodes) == n
    coefficients = get_coefficients(nodes, moments[:n])
    value = quadrature_formula(coefficients, nodes, func)
    return QuadratureResult(value, moments, polynomial, nodes, coefficients)
