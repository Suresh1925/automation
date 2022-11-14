import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\\Users\Praveen\PycharmProjects\PraveenProject\driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://developer.salesforce.com/signup")
driver.maximize_window()
driver.find_element(By.XPATH).click()