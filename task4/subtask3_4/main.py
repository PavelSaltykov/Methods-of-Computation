from decimal import Decimal

from common.cli import request_segment, request_input
from common.math import integral
from common.math.function import Function
from common.math.integral import integral2str
from task4.subtask2.polynomials import PRECISION_POLYNOMIALS
from task4.subtask3_4.quadrature import left_rectangles, right_rectangles, middle_rectangles, trapezes, simpson, get_h
from task4.subtask3_4.runge import method_runge

WEIGHT = Function("1")
FUNCTION = Function("exp(x)")
POLYNOMIAL = PRECISION_POLYNOMIALS[0]

QUADRATURES = {
    "СКФ левых прямоугольников": (left_rectangles, 0),
    "СКФ правых прямоугольников": (right_rectangles, 0),
    "СКФ средних прямоугольников": (middle_rectangles, 1),
    "СКФ трапеций": (trapezes, 1),
    "СКФ Симпсона": (simpson, 3),
}


def main():
    print("ПРИБЛИЖЁННОЕ ВЫЧИСЛЕНИЕ ИНТЕГРАЛА ПО СОСТАВНЫМ КВАДРАТУРНЫМ ФОРМУЛАМ\n")
    function = WEIGHT * FUNCTION
    print(f"Функция: f(x) = {function}")

    segment = request_segment()
    m = int(request_input(f"Введите число разбиений: m = ",
                          lambda s: (s.isdigit() and int(s) > 0, "Число должно быть больше 0")))
    print(f"h = {get_h(segment, m)}\n")

    integral_str = integral2str(function, segment)
    print(f"Интеграл: {integral_str}")

    exact = integral.exact_value(function, segment)
    print(f'"Точное" значение: {exact}')
    print()

    exact = Decimal(exact)
    results_m = []
    for name, quadrature in QUADRATURES.items():
        formula, _ = quadrature
        result, theoretical_error = formula(function, segment, m)
        results_m.append((name, quadrature, result))
        print(f"{name}: {result}")

        actual_error = abs(exact - result)
        print(f"Абсолютная фактическая погрешность: {actual_error}")

        relative_error = abs(actual_error / exact)
        print(f"Относительная фактическая погрешность: {relative_error}")

        print(f"Теоретическая погрешность: {theoretical_error}")
        print()

    print("УТОЧНЕНИЕ ЗНАЧЕНИЙ ПО ПРИНЦИПУ РУНГЕ-РОМБЕРГА\n")

    coefficient_l = int(request_input(f"Введите коэффициент числа разбиений: l = ",
                                      lambda s: (s.isdigit() and int(s) > 0, "Число должно быть больше 0")))

    ml = m * coefficient_l
    for name, quadrature, result_m in results_m:
        formula, degree = quadrature
        result_ml, _ = formula(function, segment, ml)
        print(f"{name}: {result_ml}")

        actual_error_ml = abs(exact - result_ml)
        print(f"Абсолютная фактическая погрешность: {actual_error_ml}")

        refined = method_runge(result_m, result_ml, coefficient_l, degree)
        print(f"\tУточненное значение: {refined}")

        actual_error_refined = abs(exact - refined)
        print(f"\tАбсолютная фактическая погрешность: {actual_error_refined}")

        relative_error_refined = abs(actual_error_refined / exact)
        print(f"\tОтносительная фактическая погрешность: {relative_error_refined}")
        print()


if __name__ == '__main__':
    main()
