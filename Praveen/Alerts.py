import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
name = "Rahul"
service_obj = Service("C:\\Users\Praveen\PycharmProjects\PraveenProject\driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
time.sleep(2)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept()