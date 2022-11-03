from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(2)
driver.find_element(By.LINK_TEXT, "Click Here").click()

windowsopened = driver.window_handles
# window_handles is a property to get all the window name which got opened and put it in list
# 1st window got opened will be in 0th index and goes on(get window will be the 1st window)

driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)

driver.close() # This will close only the child window as the control is in child window

driver.switch_to.window(windowsopened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)

assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text









