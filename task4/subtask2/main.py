from decimal import Decimal

from common.cli import request_segment
from common.math import integral
from common.math.function import Function
from common.math.integral import integral2str
from task4.subtask2.polynomials import PRECISION_POLYNOMIALS
from task4.subtask2.quadrature import left_rectangle, right_rectangle, middle_rectangle, trapeze, simpson, three_eighths

FUNCTION = Function("exp(x) + x")
POLYNOMIAL = PRECISION_POLYNOMIALS[0]

QUADRATURES = {
    "КФ левого прямоугольника": left_rectangle,
    "КФ правого прямоугольника": right_rectangle,
    "КФ среднего прямоугольника": middle_rectangle,
    "КФ трапеции": trapeze,
    "КФ Симпсона (или парабол)": simpson,
    "КФ 3/8": three_eighths,
}


def main():
    print("ПРИБЛИЖЁННОЕ ВЫЧИСЛЕНИЕ ИНТЕГРАЛА ПО КВАДРАТУРНЫМ ФОРМУЛАМ\n")
    print(f"Функция: f(x) = {FUNCTION}")

    segment = request_segment()
    print()

    integral_str = integral2str(FUNCTION, segment)
    print(f"Интеграл: {integral_str}")

    exact = integral.exact_value(FUNCTION, segment)
    print(f'"Точное" значение: {exact}\n')

    for name, formula in QUADRATURES.items():
        result = formula(FUNCTION, segment)
        print(f"{name}: {result}")
        print(f"Фактическая погрешность: {abs(Decimal(exact) - result)}")
        print()


if __name__ == '__main__':
    main()
