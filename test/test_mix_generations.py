from src.check_colors import mix_generations
import pytest

@pytest.mark.mix_generations
@pytest.mark.parametrize(
    "first_individiual, second_individual, first_result, second_result",
    [
        (["Red", "Red", "Red", "Red"],["Red", "Green", "Blue", "Red"], ["Red", "Red", "Blue", "Red"],["Red", "Green", "Red", "Red"]),
        (["Red", "Green", "Yellow", "Red"],["Red", "Green", "Blue", "Red"],["Red", "Green", "Blue", "Red"],["Red", "Green", "Yellow", "Red"]),
        (["Red", "Red", "Red", "Red"],["Green", "Blue", "Yellow", "Pink"], ["Red", "Red","Yellow", "Pink"],["Green", "Blue", "Red", "Red"]),
        (["Pink", "Yellow", "Blue", "Green"],["Green", "Blue", "Yellow", "Pink"], ["Pink", "Yellow","Yellow", "Pink"],["Green", "Blue", "Blue", "Green"])
    ]
)


def test_mix_generations(first_individual, second_individual,first_result,second_result):
    assert mix_generations(first_individual,second_individual) == (first_result,second_result)