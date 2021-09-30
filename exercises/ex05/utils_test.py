"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730272419"
from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_evens_odds() -> None:
    """Tests for the only_evens function."""
    toe: list[int] = [2, 4, 1, 3]
    assert only_evens(toe) == [2, 4]


def test_only_evens_all_odds() -> None:
    """Tests for the only_evens function."""
    toe: list[int] = [1, 3]
    assert only_evens(toe) == []


def test_only_evens_all_evens() -> None:
    """Tests for the only_evens function."""
    toe: list[int] = [8, 8, 8]
    assert only_evens(toe) == [8, 8, 8]


def test_sub_use() -> None:
    """Tests for sub function."""
    tsub: list[int] = [10, 20, 30]
    a: int = 0
    b: int = 2
    assert sub(tsub, a, b) == [10, 30]


def test_sub_edge_1() -> None:
    """Tests for sub function."""
    tsub: list[int] = [10, 20, 30]
    a: int = -2
    b: int = 9
    assert sub(tsub, a, b) == [10, 30]


def test_sub_edge_2() -> None:
    """Tests for sub function."""
    tsub: list[int] = []
    a: int = 9
    b: int = 0
    assert sub(tsub, a, b) == []


def test_concat_edge() -> None:
    """Tests for the concat function."""
    tconcat1: list[int] = []
    tconcat2: list[int] = []
    assert concat(tconcat1, tconcat2) == []


def test_concat_use1() -> None:
    """Tests for the concat function."""
    tconcat1: list[int] = [1, 2, 3]
    tconcat2: list[int] = [4, 5, 6]
    assert concat(tconcat1, tconcat2) == [1, 2, 3, 4, 5, 6]


def test_concat_use2() -> None:
    """Tests for the concat function."""
    tconcat1: list[int] = [1, 2, 3]
    tconcat2: list[int] = []
    assert concat(tconcat1, tconcat2) == [1, 2, 3]