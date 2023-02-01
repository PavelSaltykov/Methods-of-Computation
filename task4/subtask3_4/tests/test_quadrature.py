from decimal import Decimal

import pytest

from common.math import integral
from common.math.segment import Segment
from common.utils import round_decimal
from task4.subtask2.polynomials import PRECISION_POLYNOMIALS
from task4.subtask3_4.quadrature import left_rectangles, right_rectangles, middle_rectangles, trapezes, simpson

SEGMENT = Segment(0, 1)
M = 1000


@pytest.mark.parametrize(
    "quadrature,degree",
    [(left_rectangles, 0),
     (right_rectangles, 0),
     (middle_rectangles, 1),
     (trapezes, 1),
     (simpson, 3)]
)
def test_composite_quadrature_precision(quadrature, degree: int):
    polynomials = PRECISION_POLYNOMIALS[:degree + 1]
    for f in polynomials:
        exact = Decimal(integral.exact_value(f, SEGMENT))
        result, a = quadrature(f, SEGMENT, M)
        error = round_decimal(exact - result, 16)
        assert error == 0
