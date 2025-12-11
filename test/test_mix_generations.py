from src.mix_generations import mix_generations
import pytest

@pytest.mark.mix_generations
@pytest.mark.parametrize(
    "parents, childs",
    [
        ([["Red", "Red", "Red", "Red"],["Red", "Green", "Blue", "Red"]], [["Red", "Red", "Blue", "Red"],["Red", "Green", "Red", "Red"]]),
        ([["Red", "Green", "Yellow", "Red"],["Red", "Green", "Blue", "Red"]],[["Red", "Green", "Blue", "Red"],["Red", "Green", "Yellow", "Red"]]),
        ([["Red", "Red", "Red", "Red"],["Green", "Blue", "Yellow", "Pink"]], [["Red", "Red","Yellow", "Pink"],["Green", "Blue", "Red", "Red"]]),
        ([["Pink", "Yellow", "Blue", "Green"],["Green", "Blue", "Yellow", "Pink"]], [["Pink", "Yellow","Yellow", "Pink"],["Green", "Blue", "Blue", "Green"]])
    ]
)


def test_mix_generations(parents, childs):
    assert mix_generations(parents) == childs or childs[::-1]