import math

from common.cli import request_segment
from common.math import integral
from common.math.function import Function
from common.math.integral import integral2str
from common.math.quadrature import quadrature_formula
from common.math.segment import Segment
from task5.subtask2.gauss import get_nodes_coefficients, recalculate_node, recalculate_coefficient
from task5.subtask2.table import nodes_coefficients_table

FUNCTION = Function("cos(x ** 2)")
N = [3, 6, 7, 8]
SEGMENT = Segment(0, math.pi / 4)


def check(n: int):
    print(f"N = {n}")
    degree = 2 * n - 1
    polynomial = Function(f"x ** {degree}")
    print(f"Одночлен: {polynomial}")

    segment = Segment(-1, 1)
    exact = integral.exact_value(polynomial, segment)
    print(f'"Точное" значение: {exact}')

    nodes, coefficients = zip(*get_nodes_coefficients(n))
    value = quadrature_formula(coefficients, nodes, polynomial)
    print(f"Вычисленное значение: {value}")
    print(f"Погрешность: {abs(exact - value)}")
    print()


def main():
    print("КФ ГАУССА, ЕЕ УЗЛЫ И КОЭФФИЦИЕНТЫ. ВЫЧИСЛЕНИЕ ИНТЕГРАЛОВ ПРИ ПОМОЩИ КФ ГАУССА\n")
    for n in range(1, 9):
        print(f"N = {n}")
        nodes, coefficients = zip(*get_nodes_coefficients(n))
        print(nodes_coefficients_table(nodes, coefficients))
        print()

    print("ПРОВЕРКА")
    for n in range(3, 6):
        check(n)

    print("ВЫЧИСЛЕНИЕ ИНТЕГРАЛА")
    segment = SEGMENT
    while True:
        if not segment:
            segment = request_segment()
            print()

        integral_str = integral2str(FUNCTION, segment)
        print(f"Интеграл: {integral_str}")

        exact = integral.exact_value(FUNCTION, segment)
        print(f'"Точное" значение: {exact}')
        print()

        for n in N:
            print(f"N = {n}")
            nodes, coefficients = zip(*get_nodes_coefficients(n))
            recalculated_nodes = [recalculate_node(segment, n) for n in nodes]
            recalculated_coefficients = [recalculate_coefficient(segment, c) for c in coefficients]
            print(nodes_coefficients_table(recalculated_nodes, recalculated_coefficients))

            value = quadrature_formula(recalculated_coefficients, recalculated_nodes, FUNCTION)
            print(f"Вычисленное значение: {value}")
            print(f"Фактическая погрешность: {abs(exact - value)}")
            print()

        segment = None


if __name__ == '__main__':
    main()
