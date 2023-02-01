from common.cli import request_segment, request_input
from common.math import integral
from common.math.function import Function
from common.math.integral import integral2str
from task5.subtask2.gauss import get_nodes_coefficients
from task5.subtask2.table import nodes_coefficients_table
from task5.subtask3.quadrature import compound_gauss

WEIGHT = Function("exp(x)")
SIMPLE_FUNCTION = Function("sin(x)")


def main():
    print("ПРИБЛИЖЁННОЕ ВЫЧИСЛЕНИЕ ИНТЕГРАЛА ПРИ ПОМОЩИ СОСТАВНОЙ КФ ГАУССА\n")
    print(f"q(x) = {WEIGHT}")
    print(f"f(x) = {SIMPLE_FUNCTION}")
    print()

    segment = request_segment()
    print()

    function = WEIGHT * SIMPLE_FUNCTION
    integral_str = integral2str(function, segment)
    print(f"Интеграл: {integral_str}")

    exact = integral.exact_value(function, segment)
    print(f'"Точное" значение: {exact}')
    print()

    while True:
        n = int(request_input(f"Введите количество узлов: N = ",
                              lambda s: (s.isdigit() and int(s) > 0, "Число должно быть больше 0")))

        m = int(request_input(f"Введите число разбиений: m = ",
                              lambda s: (s.isdigit() and int(s) > 0, "Число должно быть больше 0")))

        nodes, coefficients = zip(*get_nodes_coefficients(n))
        print(nodes_coefficients_table(nodes, coefficients))

        value = compound_gauss(nodes, coefficients, segment, function, m)
        print(f"Вычисленное значение: {value}")
        print(f"Фактическая погрешность: {abs(exact - value)}")
        print()


if __name__ == '__main__':
    main()
