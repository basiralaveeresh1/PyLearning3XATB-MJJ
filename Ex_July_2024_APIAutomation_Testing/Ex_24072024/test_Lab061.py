import allure
import pytest
import requests


@allure.title("Test GET Request - RestFull Booker Project#1")
@allure.description("TC#1: Verify that GET Request with ID works")
@allure.tag("regression","P0","smoke")
@allure.label("Owner", "Veeresh B")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200

@allure.title("Test GET Request - RestFull Booker Project#1")
@allure.description("TC#2: Verify that GET Request Invalid booking id")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalidId"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404


@allure.title("Test GET Request - RestFull Booker Project#1")
@allure.description("TC#2: Verify that GET Request Invalid booking id")
@pytest.mark.smoke
def test_get_single_request_by_id_negative2():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404