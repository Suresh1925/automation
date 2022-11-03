# Frame is embeded html which sits top on base html
# the piece of the component is frame which is in another page which is embeded in parent html
# it appears to be working on parent html, but it is actually working on child which is running in background
# So driver will not have any knowledge of this child html as it is embeded, as it only knows parent html

# HOW TO KNOW THE FRAME IS IN HTML
# 1. developer will inform
# 2. Even after giving corrct path, if locators failes to find
# 3. we can find tag <iframe

from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(2)

driver.switch_to.frame("mce_0_ifr") # we can give frame id or name inside

driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("We are learning about Frame")

driver.switch_to.default_content()# this will return to original window

print(driver.find_element(By.TAG_NAME,"h3").text)






