from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(3)
getTitle = driver.title
print(getTitle)

enterText = driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Iphone")
time.sleep(3)

searchBox = driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(3)
#driver.find_element(By.LINK_TEXT,"Stay productive with the Apple products you love.").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Apple products you love.").click()
time.sleep(3)



