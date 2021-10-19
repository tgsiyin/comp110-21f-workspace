"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730272419"


def test_invert_usecase() -> None:
    """Test for the invert function."""
    ti: dict[str, str] = {'a': 'z', 'y': 'x', 'd': 'k'}
    assert invert(ti) == {'z': 'a', 'x': 'y', 'k': 'd'}


def test_invert_usecase2() -> None:
    """Test for the invert function."""
    ti: dict[str, str] = {}
    assert invert(ti) == {}


def test_invert_edgecase3() -> None:
    """Test for the invert function."""
    ti: dict[str, str] = {'a': 'z', 'b': 'z', 'd': 'k'}
    assert invert(ti) == "KeyError"


def test_favorite_color_usecase1() -> None:
    """Test for the favorite_color function."""
    tfc: dict[str, str] = {'Aaron': 'blue', 'John': 'blue', 'Kitty': 'green', 'Alex': 'purple'}
    assert favorite_color(tfc) == "blue"


def test_favorite_color_edgecase2() -> None:
    """Test for the favorite_color function."""
    tfc: dict[str, str] = {'Aaron': 'blue', 'John': 'blue', 'Kitty': 'green', 'Alex': 'green'}
    assert favorite_color(tfc) == "blue"


def test_favorite_color_usecase3() -> None:
    """Tests for the favorite_color function."""
    tfc: dict[str, str] = {'Aaron': 'blue', 'John': 'blue', 'Kitty': 'green', 'Alex': 'green', 'Helen': 'green'}
    assert favorite_color(tfc) == "green"


def test_count_usecase1() -> None:
    """Tests for the count function."""
    tc: list[str] = ["elephant", "whale", "elephant", "lion", "dolphin", "dolphin", "dolphin"]
    assert count(tc) == {'elephant': 2, "whale": 1, 'lion': 1, "dolphin": 3}


def test_count_usecase2() -> None:
    """Tests for the count function."""
    tc: list[str] = ["elephant", "whale", "lion", "dolphin"]
    assert count(tc) == {'elephant': 1, "whale": 1, 'lion': 1, "dolphin": 1}


def test_count_edgecase3() -> None:
    """Tests for the count function."""
    tc: list[str] = []
    assert count(tc) == {}