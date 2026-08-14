import pytest

def test_first_try():
    print("Hello world")

def test_assert_positive_case():
    assert 2 + 2 == 4

def test_assert_negative_case():
    assert 2 + 2 == 5

@pytest.fixture
def alt():
    return 4/0

def test_assert_error_case(alt):
    a = alt
    if a != 0:
        raise ValueError
    assert c + 2 == 5
