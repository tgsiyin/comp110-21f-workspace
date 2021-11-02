"""Utility functions."""

__author__ = "730272419"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'rable'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(x: list[dict[str, str]], y: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in x:
        item: str = row[y]
        result.append(item)
    return result


def columnar(x: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row_oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = x[0]
    for column in first_row:
        result[column] = column_values(x, column)
    
    return result


def head(x: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    """Produce a dictionary within certain range of the original dictionary."""
    result: dict[str, list[str]] = {}
    for column in x:
        if y >= len(x):
            return x
        selected: list[str] = []
        a: int = 0
        while len(selected) < y:
            selected.append(x[column][a])
            a += 1
        result[column] = selected
    return result


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Produce a dictionary with selected columns of values of original dictionary."""
    result: dict[str, list[str]] = {}
    for column in x:
        a: int = 0
        while a < len(y):
            if column == y[a]:
                result[column] = x[column]
            a += 1
    return result


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two dictionary's data together in one dictionary."""
    result: dict[str, list[str]] = {}
    for column in x:
        result[column] = x[column]
    for key in y:
        if key in result:
            result[key] += y[key]
        else:
            result[key] = y[key]
    return result
    

def count(x: list[str]) -> dict[str, int]:
    """Count the times a string values occur in a list and make a dictionary."""
    result: dict[str, int] = {}
    for key in x:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result
