from common.cli import request_segment, request_input
from common.math import integral
from common.math.function import Function
from common.math.integral import integral2str
from common.math.quadrature import quadrature_formula
from task5.subtask1.quadrature import calculate_approximate_value

WEIGHT = Function("exp(x)")
SIMPLE_FUNCTION = Function("sin(x)")


def check(n: int, moments: list[float], coefficients: list[float], nodes: list[float]):
    degree = 2 * n - 1
    polynomial = Function(f"x ** {degree}")
    print(f"Одночлен: {polynomial}")
    moment = moments[degree]
    print(f"Момент с номером {degree}: {moment}")

    value = quadrature_formula(coefficients, nodes, polynomial)
    print(f"Квадратурная сумма: {value}")
    print(f"Погрешность: {abs(moment - value)}")


def main():
    print("ВЫЧИСЛЕНИЕ ИНТЕГРАЛА ПРИ ПОМОЩИ КВАДРАТУРНОЙ ФОРМУЛЫ НАИВЫСШЕЙ АЛГЕБРАИЧЕСКОЙ СТЕПЕНИ ТОЧНОСТИ\n")
    print(f"ρ(x) = {WEIGHT}")
    print(f"f(x) = {SIMPLE_FUNCTION}")
    print()

    segment = request_segment()
    print()

    function = WEIGHT * SIMPLE_FUNCTION
    integral_str = integral2str(function, segment)
    print(f"Интеграл: {integral_str}")

    exact = integral.exact_value(function, segment)
    print(f'"Точное" значение: {exact}')

    n = int(request_input(f"Введите количество узлов: ",
                          lambda s: (s.isdigit() and int(s) > 0, "Число должно быть больше 0")))

    result = calculate_approximate_value(segment, WEIGHT, SIMPLE_FUNCTION, n)
    print()
    print(f"Моменты: {result.weight_moments}")
    print(f"Ортогональный многочлен: {result.orthogonal_polynomial}")
    print(f"Узлы: {result.quadrature_nodes}")
    print(f"Коэффициенты: {result.quadrature_coefficients}")
    print()

    print("ПРОВЕРКА")
    check(n, result.weight_moments, result.quadrature_coefficients, result.quadrature_nodes)
    print()

    value = result.value
    print(f"Вычисленное значение интеграла: {value}")
    print(f"Фактическая погрешность: {abs(exact - value)}")


if __name__ == '__main__':
    main()
