from collections.abc import Sequence


def describe(values: Sequence[float]) -> dict[str, float]:
    if not values:
        return {"count": 0.0}
    return {
        "count": float(len(values)),
        "mean": sum(values) / len(values),
        "minimum": min(values),
        "maximum": max(values),
    }
