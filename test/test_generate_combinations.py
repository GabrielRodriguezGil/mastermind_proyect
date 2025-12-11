from src.generate_combinations import generate_conbinations
import pytest

@pytest.mark.test_generate_combinations
def test_generate_combinations():
    assert len(generate_conbinations()) == 80
    
    for i in generate_conbinations():
        assert len(i) == 4
