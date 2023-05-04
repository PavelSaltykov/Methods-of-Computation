from decimal import Decimal

from mpmath import mpf
from scipy.optimize import optimize
from sympy import parse_expr, lambdify

from common.math.segment import Segment
from common.utils import to_decimal


class Function:
    def __init__(self, fun_str: str):
        self.__variable = 'x'
        self.__fun_str = fun_str
        self.__fun_expr = parse_expr(self.__fun_str)
        self.__fun_lambda = lambdify(self.__variable, self.__fun_expr, modules='mpmath')

    def derivative(self, n: int = 1) -> 'Function':
        return Function(str(self.__fun_expr.diff(self.__variable, n)))

    def get_lambda(self):
        return self.__fun_lambda

    def max(self, segment: Segment) -> Decimal:
        left = self(segment.left)
        right = self(segment.right)
        inner_max = self(Decimal(optimize.fminbound(
            lambda x: float((-self)(x)), float(segment.left), float(segment.right)
        )))
        return max(left, right, inner_max)

    def __call__(self, arg) -> Decimal:
        value = self.__fun_lambda(mpf(str(arg)))
        return to_decimal(value)

    def __str__(self) -> str:
        return str(self.__fun_expr)

    def __abs__(self) -> 'Function':
        return Function(f"abs({self})")

    def __add__(self, other) -> 'Function':
        return Function(f"({self}) + ({other})")

    def __sub__(self, other):
        return Function(f"({self}) - ({other})")

    def __mul__(self, other) -> 'Function':
        return Function(f"({self}) * ({other})")

    def __neg__(self) -> 'Function':
        return Function(f"-{self}")
