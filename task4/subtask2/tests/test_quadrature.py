from decimal import Decimal

import pytest

from common.math import integral
from common.math.segment import Segment
from common.utils import round_decimal
from task4.subtask2.polynomials import PRECISION_POLYNOMIALS
from task4.subtask2.quadrature import left_rectangle, right_rectangle, middle_rectangle, trapeze, simpson, three_eighths

SEGMENT = Segment(0, 1)


@pytest.mark.parametrize(
    "quadrature,degree",
    [(left_rectangle, 0),
     (right_rectangle, 0),
     (middle_rectangle, 1),
     (trapeze, 1),
     (simpson, 3),
     (three_eighths, 3)]
)
def test_quadrature_precision(quadrature, degree: int):
    polynomials = PRECISION_POLYNOMIALS[:degree + 1]
    for f in polynomials:
        exact = Decimal(integral.exact_value(f, SEGMENT))
        result = quadrature(f, SEGMENT)
        error = round_decimal(exact - result, 15)
        assert error == 0
