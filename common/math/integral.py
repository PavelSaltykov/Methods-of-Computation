from scipy import integrate

from common.math.function import Function
from common.math.segment import Segment


def exact_value(f: Function, segment: Segment) -> float:
    a, b = segment
    exact, *_ = integrate.quad(f.get_lambda(), float(a), float(b))
    return exact


def integral2str(f, segment: Segment) -> str:
    return f"∫{segment} ({f})dx"
