import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("TC#1:Verify Login page")
@allure.description("Login the application using username and password")
@pytest.mark.smoke
def test_katalon_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    uiText = driver.find_element(By.XPATH,"//h1[text()='CURA Healthcare Service']").text
    print(uiText)
    assert uiText == "CURA Healthcare Service"
    print("Testcase Passed")


    # allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    # assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Assertion Fail Message:  Wrong URL"
    # print(driver.current_url)
    #
    # # Xpath Locator
    # driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']").click()
    driver.quit()



