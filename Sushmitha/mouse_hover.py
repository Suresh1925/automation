import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("D:/Sushmitha/framework/python_basics/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, '//*[@id="mousehover"]')).perform()
time.sleep(2)
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).click().perform()
#action.context_click()   #right click
time.sleep(3)

driver.close()