from typing import Callable, Any, Tuple

from prettytable import PrettyTable


class TableRow:
    def __init__(self, items: dict):
        self.__items = items

    def __getitem__(self, column):
        if type(column) is int:
            return list(self.__items.values())[column]
        if type(column) is slice:
            return TableRow(self.__items[column])
        return self.__items[column]

    def __len__(self) -> int:
        return len(self.__items)

    def __str__(self) -> str:
        return str(list(self.__items.values()))


class Table:
    def __init__(self, field_names: list[str], rows: list[list] = None):
        self.__field_names = field_names
        self.__number_of_columns = len(self.__field_names)

        self.__rows: list[TableRow] = []
        if rows:
            self.add_rows(rows)

    def __create_row(self, row: list) -> TableRow:
        return TableRow(dict(zip(self.__field_names, row)))

    @property
    def field_names(self) -> list[str]:
        return self.__field_names

    @property
    def rows(self) -> list[list]:
        return list(map(list, self.__rows))

    @property
    def columns(self) -> list[list]:
        columns = []
        for column in self.field_names:
            columns.append([row[column] for row in self.__rows])
        return columns

    def add_row(self, row: list):
        if len(row) != self.__number_of_columns:
            raise ValueError(f"Row should have {self.__number_of_columns} items")

        self.__rows.append(self.__create_row(row))

    def add_rows(self, rows: list[list]):
        for row in rows:
            self.add_row(row)

    def sorted(self, key: Callable[[TableRow], Any], reverse: bool = False) -> 'Table':
        sorted_rows = list(map(list, sorted(self.__rows, key=key, reverse=reverse)))
        sorted_table = Table(self.__field_names, sorted_rows)
        return sorted_table

    def zip(self) -> list[Tuple]:
        return list(zip(*self.columns))

    def to_pretty_table(self) -> PrettyTable:
        table = PrettyTable(self.__field_names)
        table.add_rows(self.rows)
        return table

    def __str__(self) -> str:
        table = self.to_pretty_table()
        return str(table)
