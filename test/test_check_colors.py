from src.check_colors import check_colors
import pytest

@pytest.mark.check_colors
@pytest.mark.parametrize(
    "color_combination, solution, result",
    [
        (["Red", "Red", "Red", "Red"],["Red", "Green", "Blue", "Red"], 2),
        (["Red", "Green", "Blue", "Red"],["Red", "Green", "Blue", "Red"], 4),
        (["Red", "Red", "Red", "Red"],["Green", "Blue", "Yellow", "Pink"], -4),
        (["Pink", "Yellow", "Blue", "Green"],["Green", "Blue", "Yellow", "Pink"], 0)
    ]
)


def test_check_colors(color_combination, solution,result):
    assert check_colors(color_combination,solution) == result