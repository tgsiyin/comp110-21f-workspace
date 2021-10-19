"""Practice with dictionaries."""

__author__ = "730272419"
# Define your functions below
z: dict[str, int] = {}


def invert(x: dict[str, str]) -> dict[str, str]:
    """Invert function."""
    a: str = ""
    b: str = ""
    y: dict[str, str] = {}
    for key in x:
        b = x[key]
        a = key
        if b in y:
            raise KeyError("KeyError")
        else:
            y[b] = a  
    return y


def favorite_color(x: dict[str, str]) -> str:
    """favorite_color function."""
    indicator: str = ""
    j: int = 0
    k: int = 0
    y: dict[str, int] = {}
    p: str = ""
    
    for key in x:
        p = x[key]
        if p in y:
            a = int(y[p])
            y.pop(p)
            y[p] = a + 1
        else: 
            y[p] = 1
    for keyy in y:
        j = y[keyy] 
        if j >= k:
            if j > k:
                indicator = keyy
                k = j
            if j == k:
                k = j
    return indicator


def count(x: list[str]) -> dict[str, int]:
    """Count function."""
    i: int = 0
    while i < len(x):
        j: str = x[i]
        if j in z:
            a = int(z[j])
            z.pop(j)
            z[j] = a + 1
        else:
            z[j] = 1 
        i += 1
    return z