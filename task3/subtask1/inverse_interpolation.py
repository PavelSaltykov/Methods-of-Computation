from decimal import Decimal

from common.math.segment import Segment
from common.tables.table import Table
from task1.main import separate_roots
from task1.methods import bisection_method
from task2.interpolation import lagrange_interpolation
from task2.lazy import LazyInterpolationNodes


class InverseInterpolation:
    def __init__(self, table: Table):
        self.__table = table
        self.__lazy_nodes = LazyInterpolationNodes(self.__table)

        self.__reversed_table = self.__reverse_table(table)
        self.__lazy_reversed_nodes = LazyInterpolationNodes(self.__reversed_table)

    @staticmethod
    def __reverse_table(table: Table) -> Table:
        reversed_fields = list(reversed(table.field_names))
        reversed_table = Table(reversed_fields)
        for row in table.rows:
            reversed_table.add_row(list(reversed(row)))
        return reversed_table

    def reversed_table_method(self, function_value: Decimal, polynomial_degree: int) -> Decimal:
        interpolation_nodes = self.__lazy_reversed_nodes.get_nodes(function_value, polynomial_degree)
        return lagrange_interpolation(function_value, interpolation_nodes.zip())

    def equation_method(self, function_value: Decimal, polynomial_degree: int, accuracy: Decimal) -> list[Decimal]:
        interpolation_nodes = self.__lazy_nodes.get_nodes(function_value, polynomial_degree)

        def equation(x): return lagrange_interpolation(x, interpolation_nodes.zip()) - function_value

        interpolation_segment = Segment(self.__table.rows[0][0], self.__table.rows[-1][0])
        segments = separate_roots(interpolation_segment, n=1000, f=equation)
        return [bisection_method(s, equation, accuracy).approximate_solution for s in segments]
