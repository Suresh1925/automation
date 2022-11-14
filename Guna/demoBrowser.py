from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
service_obj = Service("E:/User2/Python-Automation/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)





driver.maximize_window()
driver.get("https://www.flipkart.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
