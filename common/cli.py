from decimal import Decimal
from typing import Callable

from common.math.segment import Segment
from common.utils import is_number


def request_input(message: str, *conditions: Callable[[str], tuple[bool, str]]) -> str:
    while True:
        input_str = input(message)
        states = list(map(lambda c: c(input_str), conditions))

        if all(s[0] for s in states):
            return input_str

        fail_message = next((s[1] for s in states if not s[0]))
        print(fail_message)


def request_segment() -> Segment:
    a = Decimal(request_input(f"Введите левый конец отрезка: a = ",
                              lambda s: (is_number(s), f"Введено недопустимое значение a")))
    b = Decimal(request_input(f"Введите правый конец отрезка: b = ",
                              lambda s: (is_number(s), f"Введено недопустимое значение b"),
                              lambda s: (is_number(s) and Decimal(s) > a,
                                         "Правый конец должен быть больше левого")))
    return Segment(a, b)
