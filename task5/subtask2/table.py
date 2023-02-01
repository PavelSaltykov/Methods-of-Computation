from common.tables.table import Table


def nodes_coefficients_table(nodes: list[float], coefficients: list[float]) -> Table:
    fields = ["Узел", "Коэффициент"]
    table = Table(fields)
    for n, c in zip(nodes, coefficients):
        table.add_row([n, c])
    return table
