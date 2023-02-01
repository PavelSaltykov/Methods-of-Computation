from decimal import Decimal

from common.math.function import Function
from common.math.segment import Segment
from common.tables.assistive import create_value_table, table_with_fields, print_table_with_title, \
    table_with_transformation
from common.tables.table import Table
from common.utils import to_italic
from task3.subtask2.cli import request_parameters
from task3.subtask2.numerical_differentiation import calculate_first_derivatives, calculate_second_derivatives

TITLE = "НАХОЖДЕНИЕ ПРОИЗВОДНЫХ ТАБЛИЧНО-ЗАДАННОЙ ФУНКЦИИ ПО ФОРМУЛАМ ЧИСЛЕННОГО ДИФФЕРЕНЦИРОВАНИЯ"

VARIANT = 8
K = VARIANT % 5 + 1
COEFFICIENT_OF_K = 1.5
FUNCTION_STR = f"e^({COEFFICIENT_OF_K}*{K}*x)"
FUNCTION_PYTHON = FUNCTION_STR.replace("e^", "exp")
COEFFICIENT = Decimal(COEFFICIENT_OF_K * K)

RESULT_TABLE_FIELDS = [to_italic("x"),
                       to_italic("f(x)"),
                       to_italic("f'(x)чд"),
                       f"""|{to_italic("f'(x)т - f'(x)чд")}|""",
                       f"""относительная погр-ть для {to_italic("f'")}""",
                       to_italic("f''(x)чд"),
                       f"""|{to_italic("f''(x)т - f''(x)чд")}|""",
                       f"""относительная погр-ть для {to_italic("f''")}"""]


def abs_error(precise: Decimal, approximate: Decimal) -> Decimal:
    return abs(precise - approximate)


def relative_error(abs_err: Decimal, approximate: Decimal) -> Decimal | None:
    if approximate.is_zero():
        return None
    return abs_err / abs(approximate)


def create_result_table(table: Table) -> Table:
    points = table.columns[0]
    f_values = table.columns[1]

    step = points[1] - points[0]

    derivatives1 = calculate_first_derivatives(f_values, step)
    derivatives2 = calculate_second_derivatives(f_values, step)

    result_table = Table(RESULT_TABLE_FIELDS)

    for index in range(len(points)):
        point = points[index]
        f_value = f_values[index]

        derivative1 = derivatives1[index]
        abs_error1 = abs_error(COEFFICIENT * f_value, derivative1)
        relative_error1 = relative_error(abs_error1, derivative1)

        derivative2 = derivatives2[index]
        abs_error2 = None if derivative2 is None else abs_error(COEFFICIENT * COEFFICIENT * f_value, derivative2)
        relative_error2 = None if derivative2 is None else relative_error(abs_error2, derivative2)

        row = [point, f_value, derivative1, abs_error1, relative_error1, derivative2, abs_error2, relative_error2]
        result_table.add_row(row)

    return result_table


def main():
    print(TITLE)
    print()
    print(to_italic(f"f(x) = {FUNCTION_STR}"))
    print()

    while True:
        m, a, h = request_parameters()

        segment = Segment(a, a + m * h)
        value_table = create_value_table(Function(FUNCTION_PYTHON), segment.equidistant_points(m))

        print_table_with_title("Таблица значений функции",
                               table_with_fields(value_table, list(map(to_italic, value_table.field_names))))

        result_table = create_result_table(value_table)
        result_table_to_print = table_with_transformation(result_table, lambda item: "—" if item is None else item)
        print_table_with_title("Таблица результатов", result_table_to_print)

        print("Ввод новых значений параметров")


if __name__ == '__main__':
    main()
