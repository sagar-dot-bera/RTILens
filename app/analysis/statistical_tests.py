from collections.abc import Sequence


def difference_of_means(first: Sequence[float], second: Sequence[float]) -> float:
    if not first or not second:
        raise ValueError("Both samples must contain at least one value")
    return sum(first) / len(first) - sum(second) / len(second)
