import pytest


def test_cdeprg():
    print("Hello")

@pytest.mark.smoker
def test_defprg():
    print("Good morning")