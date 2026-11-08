from collections.abc import Sequence
from math import sqrt


def pearson_correlation(first: Sequence[float], second: Sequence[float]) -> float:
    if len(first) != len(second) or len(first) < 2:
        raise ValueError("Both series must have the same length and contain at least two values")
    first_mean = sum(first) / len(first)
    second_mean = sum(second) / len(second)
    numerator = sum((x - first_mean) * (y - second_mean) for x, y in zip(first, second))
    denominator = sqrt(
        sum((x - first_mean) ** 2 for x in first)
        * sum((y - second_mean) ** 2 for y in second)
    )
    if denominator == 0:
        raise ValueError("Correlation is undefined for a constant series")
    return numerator / denominator
