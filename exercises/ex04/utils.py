"""List utility functions."""

__author__ = "730272419"


# TODO: Implement your functions here.


def all(x: list[int], y: int) -> bool:
    """All function to find if all integers in a list is equal to a particular integer."""
    count: int = 0
    if len(x) > 0:
        while count < len(x):
            if x[count] != y:
                return False
            count += 1
        return True
    return False


def is_equal(x: list[int], y: list[int]) -> bool:
    """is_equal function to find if two input lists are equal."""
    count: int = 0
    if len(x) == len(y):
        if len(x) == 0 and len(y) == 0:
            return True
        while count < len(x):
            if x[count] == y[count]:
                return True
            count += 1
        return False
    return False


def max(x: list[int]) -> int:
    """The max function to find the maximum number in a list."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    larger: int = x[0]
    count: int = 0
    while count < len(x):
        if larger < x[count]:
            larger = x[count]
        count += 1
    return larger