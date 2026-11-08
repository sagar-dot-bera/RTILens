from collections.abc import Sequence


def linear_trend(values: Sequence[float]) -> float:
    if len(values) < 2:
        raise ValueError("At least two values are required")
    x_mean = (len(values) - 1) / 2
    y_mean = sum(values) / len(values)
    numerator = sum((index - x_mean) * (value - y_mean) for index, value in enumerate(values))
    denominator = sum((index - x_mean) ** 2 for index in range(len(values)))
    return numerator / denominator
