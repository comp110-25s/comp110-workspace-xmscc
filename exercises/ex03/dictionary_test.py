from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_empty():
    """Edge case: inverting an empty dictionary should return an empty dictionary."""
    assert invert({}) == {}


def test_invert_regular():
    """Use case: invert a simple dictionary with unique values."""
    assert invert({"a": "x", "b": "y"}) == {"x": "a", "y": "b"}


def test_invert_single_pair():
    """Use case: invert a dictionary with one key-value pair."""
    assert invert({"one": "1"}) == {"1": "one"}


def test_count_empty():
    """Edge case: count on an empty list should return an empty dictionary."""
    assert count([]) == {}


def test_count_multiple():
    """Use case: count elements that repeat."""
    assert count(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}


def test_count_unique():
    """Use case: count with all unique elements."""
    assert count(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


def test_favorite_color_empty():
    """Edge case: empty dictionary should return an empty string."""
    assert favorite_color({}) == ""


def test_favorite_color_tie():
    """Use case: tie for most frequent color, return the first color encountered."""
    assert favorite_color({"A": "red", "B": "blue", "C": "red", "D": "blue"}) == "red"


def test_favorite_color_clear_winner():
    """Use case: one color appears more than others."""
    assert favorite_color({"Alice": "green", "Bob": "green", "Cara": "blue"}) == "green"


def test_bin_len_empty():
    """Edge case: input list is empty, so result should be empty."""
    assert bin_len([]) == {}


def test_bin_len_normal():
    """Use case: words of different lengths grouped correctly."""
    assert bin_len(["hi", "cat", "sun"]) == {2: {"hi"}, 3: {"cat", "sun"}}


def test_bin_len_repeats():
    """Use case: duplicates in input list still result in unique set values."""
    assert bin_len(["go", "go", "stop"]) == {2: {"go"}, 4: {"stop"}}
