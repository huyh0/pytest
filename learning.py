import pytest

@pytest.fixture # Runs the fixture before every test case that needs it
def sample_scores():
    return [80, 90, 100]

def test_max_scores(sample_scores):
    assert max(sample_scores) == 100

def test_len_scores(sample_scores):
    assert len(sample_scores) == 3

def validate_score(score):
    if 0 <= score <= 100:
        return score
    else:
        raise ValueError("Score must be between 0 and 100")
    
@pytest.mark.parametrize("score,expected", [(80, 80), (0,0), (100,100)])
def test_equality(score, expected):
    assert validate_score(score) == expected

@pytest.mark.parametrize("score", [(-1), (101)])
def test_invalid(score):
    with pytest.raises(ValueError):
        validate_score(score)