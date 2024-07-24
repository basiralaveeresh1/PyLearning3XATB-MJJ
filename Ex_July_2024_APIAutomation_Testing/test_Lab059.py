import pytest

@pytest.mark.smoke
def test_substraction0():
    assert 5-5 == 0

@pytest.mark.regression
def test_substraction1():
    assert 2-2 == 0

@pytest.mark.smoke
def test_substraction2():
    assert 3-3 == 0

@pytest.mark.skip
def test_substraction3(reason = "Not working, Skip it"):
    assert 3-3 == 0
