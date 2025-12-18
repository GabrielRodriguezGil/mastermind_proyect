import sys
sys.path.append("..")
from src.mix_generations import mix_generations
import pytest

@pytest.mark.mix_generations
@pytest.mark.parametrize(
    "parents, childs",
    [
        ([["Red", "Red", "Red", "Red"],["Red", "Green", "Blue", "Red"]], [["Red", "Green", "Red", "Red"],["Red", "Red", "Blue", "Red"]]),
        ([["Red", "Green", "Yellow", "Red"],["Red", "Green", "Blue", "Red"]],[["Red", "Green", "Yellow", "Red"],["Red", "Green", "Blue", "Red"]]),
        ([["Red", "Red", "Red", "Red"],["Green", "Blue", "Yellow", "Pink"]], [["Red", "Blue","Red", "Pink"],["Green", "Red", "Yellow", "Red"]]),
        ([["Pink", "Yellow", "Blue", "Green"],["Green", "Blue", "Yellow", "Pink"]], [["Pink", "Blue","Blue", "Pink"],["Green", "Yellow", "Yellow", "Green"]])
    ]
)


def test_mix_generations(parents, childs):
    assert mix_generations(parents) == childs or childs[::-1]