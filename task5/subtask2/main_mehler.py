from common.cli import request_input
from common.math import integral
from common.math.function import Function
from common.math.integral import integral2str
from common.math.quadrature import quadrature_formula
from task5.subtask2.mehler import SEGMENT, WEIGHT, get_nodes_coefficients
from task5.subtask2.table import nodes_coefficients_table

FUNCTION = Function("exp(x) * sin(x ** 2)")


def main():
    print("КФ МЕЛЕРА, ЕЕ УЗЛЫ И КОЭФФИЦИЕНТЫ. ВЫЧИСЛЕНИЕ ИНТЕГРАЛОВ ПРИ ПОМОЩИ КФ МЕЛЕРА\n")

    function = WEIGHT * FUNCTION
    integral_str = integral2str(function, SEGMENT)
    print(f"Интеграл: {integral_str}")

    exact = integral.exact_value(function, SEGMENT)
    print(f'"Точное" значение: {exact}')
    print()

    while True:
        n = int(request_input(f"Введите количество узлов: N = ",
                              lambda s: (s.isdigit() and int(s) > 0, "Число должно быть больше 0")))

        nodes, coefficients = zip(*get_nodes_coefficients(n))
        print(nodes_coefficients_table(nodes, coefficients))

        value = quadrature_formula(coefficients, nodes, FUNCTION)
        print(f"Вычисленное значение: {value}")
        print(f"Фактическая погрешность: {abs(exact - value)}")
        print()


if __name__ == '__main__':
    main()
