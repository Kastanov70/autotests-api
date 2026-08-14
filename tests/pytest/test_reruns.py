import random
import pytest

PLATFORM = "Linux"


@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_reruns():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=5)
class TestReruns:
    def test_reruns1(self):
        assert random.choice([True, False])

    def test_reruns2(self):
        assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=5, condition=PLATFORM == "Windows")
def test_reruns_with_condition():
    assert random.choice([True, False])