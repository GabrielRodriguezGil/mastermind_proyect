from src.generate_combinations import generate_conbinations
from src.global_constants import POPULATION_SIZE
import pytest

@pytest.mark.test_generate_combinations
def test_generate_combinations():
    assert len(generate_conbinations()) == POPULATION_SIZE
    
    for i in generate_conbinations():
        assert len(i) == 4
