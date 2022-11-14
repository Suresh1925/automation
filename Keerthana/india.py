
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
from selenium.webdriver.common.by import By
import time

service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@class="inputs ui-autocomplete-input"]').send_keys("Ind")
time.sleep(2)
p = driver.find_elements(By.XPATH, '//*[@class="ui-menu-item"]/div')
print(len(p))
for place in p:
    if place.text == "India":
        place.click()
        break

time.sleep(2)
driver.close()