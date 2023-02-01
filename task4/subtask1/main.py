from common.math import integral
from common.math.function import Function
from common.math.integral import integral2str
from common.math.segment import Segment
from common.math.quadrature import get_moments, get_coefficients, quadrature_formula

INTEGRAL_FUNCTION = Function("sin(x)/sqrt(1-x)")
INTEGRAL_LEFT_POINT = 0
INTEGRAL_RIGHT_POINT = 1
WEIGHT = Function("1/sqrt(1-x)")
SIMPLE_FUNCTION = Function("sin(x)")
NODES = [1/6, 1/2, 5/6]


def main():
    print("ВЫЧИСЛЕНИЕ ИНТЕГРАЛА ПРИ ПОМОЩИ ИНТЕРПОЛЯЦИОННОЙ КВАДРАТУРНОЙ ФОРМУЛЫ\n")

    segment = Segment(INTEGRAL_LEFT_POINT, INTEGRAL_RIGHT_POINT)
    integral_str = integral2str(INTEGRAL_FUNCTION, segment)
    print(f"Интеграл: {integral_str}")

    print(f"Вес: q(x) = {WEIGHT}")
    print(f"Узлы: {NODES}")
    print()

    exact = integral.exact_value(INTEGRAL_FUNCTION, segment)
    print(f'"Точное" значение: {exact}')

    moments = get_moments(segment, WEIGHT, len(NODES))
    print(f"Моменты: {moments}")

    coefficients = get_coefficients(NODES, moments)
    print(f"Коэффициенты: {coefficients}")

    result = quadrature_formula(coefficients, NODES, SIMPLE_FUNCTION)
    print(f"Вычисленное значение: {result}")
    print(f"Фактическая погрешность: {abs(exact - result)}")


if __name__ == '__main__':
    main()
