"""
Some helper functions used throughout the scheduler.
"""
from collections import OrderedDict
from prettytable import PrettyTable
    
    
def format_for_print(df):    
    table = PrettyTable(list(df.columns))
    for row in df.itertuples():
        table.add_row(row[1:])
    return str(table)


def sort_dict_by_mrv(d):
    """Sort dictionary according to minimun remaining values heuristic."""
    return OrderedDict(sorted(d.items(), key=lambda x: len(x[1]) if isinstance(x[1], set) else 0))








