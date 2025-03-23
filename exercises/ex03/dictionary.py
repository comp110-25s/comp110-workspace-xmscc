"""Dictionary practice!"""

__author__: str = "730824666"


def invert(inverse_set: dict[str, str]) -> dict[str, str]:
    result = {}
    for key in inverse_set:
        value = inverse_set[key]
        if value in result:
            raise KeyError(f"Duplicate key encountered when inverting: {value}")
        result[value] = key
    return result


def count(values: list[str]) -> dict[str, int]:
    result = {}
    idx = 0
    while idx < len(values):
        value = values[idx]
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
        idx += 1
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    counts = {}
    for key in favorites:
        color = favorites[key]
        if color in counts:
            counts[color] += 1
        else:
            counts[color] = 1

    max_color = ""
    max_count = 0
    for key in favorites:
        color = favorites[key]
        if counts[color] > max_count:
            max_color = color
            max_count = counts[color]

    return max_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    result = {}
    i = 0
    while i < len(words):
        word = words[i]
        length = len(word)
        if length in result:
            if word not in result[length]:
                result[length] = set(list(result[length]) + [word])
        else:
            result[length] = {word}
        i += 1
    return result
