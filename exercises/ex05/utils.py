"""List utility functions part 2."""

__author__ = "730272419"

# Define your functions below


def only_evens(x: list[int]) -> list[int]:
    """The only_evens function to catch even numbers in a list."""
    i: int = 0
    a: list[int] = []
    o: int
    while i < len(x):
        if x[i] % 2 == 0:
            o = x[i]
            a.append(o)
        i += 1
    return a


def sub(x: list[int], a: int, b: int) -> list[int]:
    """The sub function to catch specific places' list elements indicates by two ints."""
    z: list[int] = []
    o: int
    p: int = len(x)
    if len(x) <= 0 or b <= 0 or a >= p:
        return []
    if a < 0:
        o = x[0]
        z.append(o)
    else:
        f: int = x[a]
        z.append(f)
    if b >= p:
        z.append(x[p - 1])
    else:
        z.append(b)
    return z


def concat(x: list[int], y: list[int]) -> list[int]:
    """The concat function to concat two lists."""
    z: list[int] = x + y
    return z