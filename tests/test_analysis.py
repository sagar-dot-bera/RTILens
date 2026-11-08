from app.analysis.correlation import pearson_correlation
from app.analysis.descriptive import describe
from app.analysis.trend import linear_trend


def test_describe() -> None:
    assert describe([1, 2, 3])["mean"] == 2


def test_correlation() -> None:
    assert pearson_correlation([1, 2, 3], [2, 4, 6]) == 1


def test_linear_trend() -> None:
    assert linear_trend([1, 3, 5]) == 2
