from decimal import Decimal
from typing import Tuple

from common.cli import request_input
from common.utils import to_italic, is_number


def request_parameters() -> Tuple[int, Decimal, Decimal]:
    number_of_values = request_input(f"Введите количество значений в таблице: {to_italic('m + 1')} = ",
                                     lambda s: (s.isdigit() and int(s) >= 3, "Число должно быть ≥ 3"))
    m = int(number_of_values) - 1

    a = Decimal(request_input(f"Введите первый узел: {to_italic('a')} = ",
                              lambda s: (is_number(s), f"Введено недопустимое значение {to_italic('a')}")))

    h = Decimal(request_input(f"Введите шаг: {to_italic('h')} = ",
                              lambda s: (is_number(s) and Decimal(s) > 0, f"Шаг должен быть больше 0")))

    return m, a, h
