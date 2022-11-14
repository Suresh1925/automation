import time
from selenium import webdriver
from selenium.webdriver import ActionChains
#chromedriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
service_obj = Service("C:\\Users\Praveen\PycharmProjects\PraveenProject\driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()
# 5 seconds is max time out.. 2 seconds (3 seconds save)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpen = driver.window_handles
driver.switch_to.window(windowsOpen[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windowsOpen[0])
assert "opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
