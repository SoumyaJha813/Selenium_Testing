import pytest


def test_cdeprg():
    print("Hello")

@pytest.mark.smoke
def test_defprg():
    print("Good morning")