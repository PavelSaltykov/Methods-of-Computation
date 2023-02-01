from common.math.function import Function
from common.math.segment import Segment
from common.utils import normalize
from task1.methods import bisection_method, newton_method, modified_newton_method, secant_method
from task1.parameters import A, B, function, accuracy, N

TITLE = "ЧИСЛЕННЫЕ МЕТОДЫ РЕШЕНИЯ НЕЛИНЕЙНЫХ УРАВНЕНИЙ"

SEGMENT = Segment(A, B)
FUNCTION = Function(function)

METHODS = {
    "Метод половинного деления": bisection_method,
    "Метод Ньютона": newton_method,
    "Модифицированный метод Ньютона": modified_newton_method,
    "Метод секущих": secant_method,
}


def print_parameters():
    print("\tИсходные параметры задачи:")
    print(f"[A, B] = {SEGMENT}")
    print(f"f(x) = {function}")
    print(f"ε = {accuracy}")


def separate_roots(segment: Segment, n: int, f) -> list[Segment]:
    segments = segment.split(n)
    roots = []

    for index in range(len(segments)):
        s = segments[index]
        if f(s.left) * f(s.right) < 0:
            roots.append(s)
            continue
        if f(s.left) == 0:
            roots.append(s)
            continue
        if f(s.right) == 0 and index == len(segments) - 1:
            roots.append(s)

    return roots


def main():
    print(TITLE)
    print()

    print_parameters()
    print()

    print("\tОтрезки перемены знака функции:")
    segments = separate_roots(SEGMENT, N, FUNCTION)
    print(f"Количество: {len(segments)}")
    for segment in segments:
        print(str(segment))
    print()

    for segment in segments:
        for method_name, method in METHODS.items():
            print(f"\t{method_name}")
            print(f"Отрезок: {segment}")
            results = method(segment, FUNCTION, accuracy)
            print(f"Начальное приближение: "
                  f"{', '.join(map(lambda x: str(normalize(x)), results.initial_approximation))}")
            print(f"Количество шагов: {results.number_of_step}")
            print(f"Приближённое решение: {normalize(results.approximate_solution)}")
            print(f"|xₘ - xₘ₋₁| = {normalize(results.delta)}")
            print(f"Абсолютная величина невязки: {normalize(abs(FUNCTION(results.approximate_solution)))}")
            print()


if __name__ == '__main__':
    main()
