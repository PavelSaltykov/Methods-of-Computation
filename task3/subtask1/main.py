from decimal import Decimal

from common.cli import request_input
from common.math.function import Function
from common.tables.assistive import create_value_table, print_table_with_title, table_with_fields
from common.utils import to_italic, is_number, normalize
from inverse_interpolation import InverseInterpolation
from task2.cli import request_preparatory_parameters, request_n

FUNCTION_STR = "2*sin(x) - x/2"


def print_results(function: Function, approximate_points: list[Decimal], function_value: Decimal):
    if not approximate_points:
        print("Решения не найдены")
    else:
        for point in approximate_points:
            print(f"Приближенное решение: {normalize(point)}")
            print(f"Модуль невязки: {normalize(abs(function(point) - function_value))}")
    print()


def main():
    print("ЗАДАЧА ОБРАТНОГО ИНТЕРПОЛИРОВАНИЯ\n")
    print(f"f(x) = {FUNCTION_STR}\n")

    m, segment = request_preparatory_parameters()

    function = Function(FUNCTION_STR)
    table = create_value_table(function, segment.equidistant_points(m))
    print_table_with_title("Таблица значений функции",
                           table_with_fields(table, list(map(to_italic, table.field_names))))

    interpolation = InverseInterpolation(table)
    while True:
        function_value = Decimal(request_input(f"Введите значение функции: {to_italic('F')} = ",
                                               lambda s: (is_number(s),
                                                          f"Введено недопустимое значение {to_italic('F')}")))

        print()
        print("1 способ: перестановка столбцов в таблице")
        n = request_n(m)
        reversed_table_result = interpolation.reversed_table_method(function_value, n)
        print_results(function, [reversed_table_result], function_value)

        print("2 способ: решение уравнения")
        n = request_n(m)
        accuracy = Decimal(request_input(f"Введите точность: {to_italic('ε')} = ",
                                         lambda s: (is_number(s) and Decimal(s) > 0,
                                                    f"Введено недопустимое значение {to_italic('ε')}")))

        equation_results = interpolation.equation_method(function_value, n, accuracy)
        print_results(function, equation_results, function_value)
        print("Ввод новых значений параметров")


if __name__ == '__main__':
    main()
