from decimal import Decimal

from common.tables.table import Table


class LazyInterpolationNodes:
    def __init__(self, table: Table):
        self.__table = table
        self.__sorted_table = self.__table
        self.__nodes = self.__sorted_table

        self.__x = None
        self.__n = None

    def get_nodes(self, x: Decimal, n: int) -> Table:
        if x == self.__x and n == self.__n:
            return self.__nodes
        if x != self.__x:
            self.__x = x
            self.__update_sorted_table()
        if n != self.__n:
            self.__n = n

        self.__update_nodes()
        return self.__nodes

    def __update_sorted_table(self):
        self.__sorted_table = self.__table.sorted(lambda row: abs(row[0] - self.__x))

    def __update_nodes(self):
        self.__nodes = Table(self.__sorted_table.field_names, self.__sorted_table.rows[:self.__n + 1])
