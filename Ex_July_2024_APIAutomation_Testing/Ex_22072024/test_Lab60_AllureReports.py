import pytest
import allure

@allure.title("Smoke Testcases: TC#1  Verify that  5-5 is equal to 0 ")
@allure.description("This is a Smoke test cases which we can verify the 5-5 equal to 0")

@pytest.mark.smoke
def test_substraction0():
    assert 5-5 == 0

@allure.title("Regression Testcases: TC#2  Verify that  2-2 is equal to 0 ")
@allure.description("This is a Regression test cases which we can verify the 2-2 equal to 0")
@pytest.mark.regression
def test_substraction1():
    assert 2-2 == 0
@allure.title("Smoke Testcases: TC#3  Verify that  3-3 is equal to 0 ")
@allure.description("This is a Smoke test cases which we can verify the 3-3 equal to 0")
@pytest.mark.smoke

def test_substraction2():
    assert 3-3 == 0

@pytest.mark.skip
def test_substraction3(reason = "Not working, Skip it"):
    assert 3-3 == 0
