from src.check_colors import check_colors
import pytest

@pytest.mark.check_colors
@pytest.mark.parametrize(
    "color_combination, solution, result",
    [
        (["Red", "Red", "Red", "Red"],["Red", "Green", "Blue", "Red"], 10),
        (["Red", "Green", "Blue", "Red"],["Red", "Green", "Blue", "Red"], 16),
        (["Red", "Red", "Red", "Red"],["Green", "Blue", "Yellow", "Pink"], 4),
        (["Pink", "Yellow", "Blue", "Green"],["Green", "Blue", "Yellow", "Pink"],8),
        (["Red", "Red", "Red", "Red"], ["Green", "Green", "Green", "Green"],4), 
        (["Red", "Green", "Blue", "Yellow"], ["Red", "Blue", "Green", "Yellow"],12),
        (["Red", "Red", "Green", "Green"], ["Red", "Green", "Red", "Green"],12),
        (["Red", "Red", "Red", "Red"], ["Red", "Green", "Blue", "Red"],10), 
        (["Red", "Green", "Blue", "Yellow"], ["Red", "Green", "Blue", "Pink"],13),
        (["Yellow", "Blue", "Green", "Red"], ["Red", "Green", "Blue", "Yellow"],8) 
    ]
)


def test_check_colors(color_combination, solution,result):
    assert check_colors(color_combination,solution) == result