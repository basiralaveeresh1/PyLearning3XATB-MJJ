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
    # ID locator
    #driver.find_element(By.ID,"btn-make-appointment").click()
    #LINK_TEXT locator
    #makeAppointment_btn = driver.find_element(By.LINK_TEXT,"Make Appointment")

    # PARTIAL_LINK_TEXT
    # makeAppointment_btn = driver.find_element(By.PARTIAL_LINK_TEXT,"Make")
    # makeAppointment_btn.click()
    time.sleep(5)
    # Tagnanme locator
    list_of_tags = driver.find_elements(By.TAG_NAME,"a")

    list_of_tags[5].click()
    # makeAppointment_btn.click()
    time.sleep(3)
    username = driver.find_element(By.NAME,"username")
    username.send_keys("Veeresh")
    password = driver.find_element(By.NAME,"password")
    password.send_keys("Reset@123")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Assertion Fail Message:  Wrong URL"
    print(driver.current_url)

    #Xpath Locator
    driver.find_element(By.XPATH,"//a[@id='btn-make-appointment']").click()
    driver.quit()



