from common.math.function import Function
from common.math.quadrature import quadrature_formula
from common.math.segment import Segment
from task5.subtask2.gauss import recalculate_node, recalculate_coefficient


def compound_gauss(nodes: list[float], coefficients: list[float], segment: Segment, func: Function, m: int) -> float:
    segments = segment.split(m)
    result = 0
    for s in segments:
        recalculated_nodes = [recalculate_node(s, n) for n in nodes]
        recalculated_coefficients = [recalculate_coefficient(s, c) for c in coefficients]
        result += quadrature_formula(recalculated_coefficients, recalculated_nodes, func)
    return result
