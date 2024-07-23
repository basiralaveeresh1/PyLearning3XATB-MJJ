from selenium import webdriver


class Test1:
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    print(driver.title)


t = Test1()