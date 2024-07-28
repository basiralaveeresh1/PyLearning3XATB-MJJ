import requests
import pytest
import allure

@allure.title("GET: Retrive all the details")
@allure.description("TC#1: Verify GET Request with ID")

def test_get_user_details():
    url = 'https://w3schools.com'
    responceDate1 = requests.get(url)
    print(responceDate1.status_code)
    assert responceDate1.status_code == 200