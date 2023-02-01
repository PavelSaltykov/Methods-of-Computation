import numpy as np

from common.math import integral
from common.math.function import Function
from common.math.segment import Segment


def get_moments(segment: Segment, weight: Function, amount: int) -> list[float]:
    results = []
    for power in range(amount):
        func = weight * Function(f"x ** {power}")

        result = integral.exact_value(func, segment)
        results.append(result)
    return results


def get_coefficients(nodes: list[float], moments: list[float]) -> list[float]:
    matrix = []
    for power in range(len(nodes)):
        matrix.append([pow(x, power) for x in nodes])
    return list(np.linalg.solve(matrix, moments))


def quadrature_formula(coefficients: list[float], nodes: list[float], func: Function) -> float:
    coefficients_nodes = zip(coefficients, nodes)
    return sum([coefficient * float(func(node)) for coefficient, node in coefficients_nodes])
