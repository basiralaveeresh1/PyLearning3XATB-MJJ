from selenium import webdriver
import time

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
#driver = webdriver.Ie()
driver.get("https://www.w3schools.com/python/python_getstarted.asp")
driver.maximize_window()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)
getTitle = driver.title
print(getTitle)
driver.close()