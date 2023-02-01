from common.math.function import Function
from common.tables.assistive import create_value_table, table_with_fields, print_table_with_title
from common.utils import to_italic
from task2.cli import print_info, request_preparatory_parameters, request_interpolation_parameters, print_results, \
    request_new_interpolation_parameters, print_interpolation_nodes
from task2.lazy import LazyInterpolationNodes

FUNCTION_STR = "2*sin(x) - x/2"
# FUNCTION_STR = "4*x**3 - 2.6*x**2 + 0.2*x + 3"


def main():
    print_info(FUNCTION_STR)
    print()

    m, segment = request_preparatory_parameters()

    f = Function(FUNCTION_STR)
    table = create_value_table(f, segment.equidistant_points(m))
    print_table_with_title("Таблица значений функции",
                           table_with_fields(table, list(map(to_italic, table.field_names))))

    x, n = request_interpolation_parameters(m)

    lazy_nodes = LazyInterpolationNodes(table)

    interpolation_nodes = lazy_nodes.get_nodes(x, n)
    print_interpolation_nodes(interpolation_nodes)

    print_results(f, x, interpolation_nodes.zip())

    while True:
        new_parameters = request_new_interpolation_parameters(m)
        if new_parameters is None:
            break

        new_x, new_n = new_parameters

        x = x if new_x == x or new_x is None else new_x
        n = n if new_n == n or new_n is None else new_n

        interpolation_nodes = lazy_nodes.get_nodes(x, n)
        print_interpolation_nodes(interpolation_nodes)

        print_results(f, x, interpolation_nodes.zip())


if __name__ == '__main__':
    main()
