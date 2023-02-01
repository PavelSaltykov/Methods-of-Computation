from decimal import Decimal
from typing import Callable, Any

from common.math.function import Function
from common.tables.table import Table

TABLE_FIELDS = ["x_j", "f(x_j)"]


def create_value_table(f: Function, points: list[Decimal], fields: list[str] = None) -> Table:
    if fields is None:
        fields = TABLE_FIELDS
    table = Table(fields)
    for x in points:
        table.add_row([x, f(x)])
    return table


def table_with_fields(table: Table, fields: list[str]) -> Table:
    if len(fields) != len(table.field_names):
        raise ValueError("Number of new fields should be equal number of table fields")
    return Table(fields, table.rows)


def table_with_transformation(table: Table, transform_item: Callable[[Any], Any]) -> Table:
    return Table(table.field_names, list(map(lambda r: list(map(transform_item, r)), table.rows)))


def print_table_with_title(title: str, table: Table):
    print(title)
    print(table)
    print()
