import math

from common.math.function import Function
from common.math.segment import Segment

WEIGHT = Function("1/sqrt(1 - x ** 2)")
SEGMENT = Segment(-1, 1)


def get_nodes_coefficients(n: int) -> list[tuple[float, float]]:
    def get_nodes() -> list[float]:
        nodes = []
        for k in range(1, n + 1):
            node = math.cos((2 * k - 1) / (2 * n) * math.pi)
            nodes.append(node)
        return nodes

    coefficient = math.pi / n
    return [(n, coefficient) for n in get_nodes()]
