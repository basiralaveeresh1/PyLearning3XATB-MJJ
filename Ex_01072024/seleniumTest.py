import time

from selenium import webdriver


class Test1:
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    print(driver.title)
    assert driver.title == "Google"
    print("The test is Pass")
    time.sleep(5)


t = Test1()