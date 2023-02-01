from decimal import Decimal
from typing import Tuple

from common.cli import request_input, request_segment
from common.math.function import Function
from common.math.segment import Segment
from common.tables.assistive import table_with_fields, print_table_with_title
from common.tables.table import Table
from common.utils import is_number, to_italic, normalize
from task2.interpolation import lagrange_interpolation, newton_interpolation


def print_info(f: str):
    print("ЗАДАЧА АЛГЕБРАИЧЕСКОГО ИНТЕРПОЛИРОВАНИЯ\n")
    print(f"Номер варианта: 8")
    print(to_italic(f"f(x) = {f}"))


def request_preparatory_parameters() -> Tuple[int, Segment]:
    number_of_values = request_input(f"Введите количество значений в таблице: {to_italic('m + 1')} = ",
                                     lambda s: (s.isdigit() and int(s) >= 2, "Число должно быть ≥ 2"))
    m = int(number_of_values) - 1
    segment = request_segment()
    print(f"Отрезок: {segment}\n")
    return m, segment


def request_x() -> Decimal:
    return Decimal(request_input(f"Введите точку интерполирования: {to_italic('x')} = ",
                                 lambda s: (is_number(s), f"Введено недопустимое значение {to_italic('x')}")))


def request_n(m: int) -> int:
    return int(request_input(f"Введите степень интерполяционного многочлена "
                             f"({to_italic(f'n ≤ {m}')}): {to_italic('n')} = ",
                             lambda s: (s.isdigit() and int(s) <= m,
                                        f"Введено недопустимое значение {to_italic('n')}")))


def request_interpolation_parameters(m: int) -> Tuple[Decimal, int]:
    x = request_x()
    n = request_n(m)
    print()
    return x, n


def print_interpolation_nodes(nodes: Table):
    print_table_with_title("Узлы интерполяции", table_with_fields(nodes, list(map(to_italic, nodes.field_names))))


def print_results(f: Function, x: Decimal, values: list[Tuple[Decimal, Decimal]]):
    fx = f(x)

    lagrange_result = lagrange_interpolation(x, values)
    print(f"Значение интерполяционного многочлена в форме Лагранжа: {normalize(lagrange_result)}")
    print(f"Значение абсолютной фактической погрешности для формы Лагранжа: {normalize(abs(fx - lagrange_result))}")
    print()

    newton_result = newton_interpolation(x, values)
    print(f"Значение интерполяционного многочлена в форме Ньютона:  {normalize(newton_result)}")
    print(f"Значение абсолютной фактической погрешности для формы Ньютона: {normalize(abs(fx - newton_result))}")
    print()


def request_new_interpolation_parameters(m: int) -> Tuple[Decimal | None, int | None] | None:
    commands = {
        'new x': 'x',
        'new n': 'n',
        'result': 'r',
        'exit': 'q'
    }

    def print_commands():
        print()
        print("Введите:")
        print(f"\t'{commands['new x']}' для ввода нового {to_italic('x')}")
        print(f"\t'{commands['new n']}' для ввода нового {to_italic('n')}")
        print(f"\t'{commands['result']}', чтобы показать результаты")
        print(f"\t'{commands['exit']}' для выхода")

    new_x = None
    new_n = None

    while True:
        print_commands()
        input_command = input()
        if input_command == commands['new x']:
            new_x = request_x()
        elif input_command == commands['new n']:
            new_n = request_n(m)
        elif input_command == commands['result']:
            return new_x, new_n
        elif input_command == commands['exit']:
            return None
        else:
            print("Введена неизвестная команда")
