import time
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("D:/Sushmitha/framework/python_basics/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("http://13.233.96.83/interface/login/login.php?site=default")
time.sleep(2)

#XPATH = //tagname[@attribute='value']
#CSS = tagname[attribute='value']
driver.find_element(By.NAME, "authUser").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,'*[type="password"]').clear()
driver.find_element(By.XPATH,'//*[@type="password"]').send_keys("openemr@2022")
driver.find_element(By.ID, "login-button").click()
