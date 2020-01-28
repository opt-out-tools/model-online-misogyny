import pytest


@pytest.fixture
def test_tweet_1_json():
    return '{"id": 1, "text": "Alice Tweet", "user": {"id": 11, "name": "Alice", "location": "Berlin"}}'


@pytest.fixture
def test_tweet_2_json():
    return '{"id": 2, "text": "Bob Tweet", "user": {"id": 22, "name": "Bob"}}'


@pytest.fixture
def test_tweet_3_json():
    """Identical to test_tweet_2_json but with a different Tweet id."""
    return '{"id": 3, "text": "Bob Tweet", "user": {"id": 22, "name": "Bob"}}'
