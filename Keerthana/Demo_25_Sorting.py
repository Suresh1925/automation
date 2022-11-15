from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object #service is a class
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(2)

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
NewList = []
VegLists = driver.find_elements(By.XPATH, "//td[1]") # //tbody/tr
for VegList in VegLists:
    NewList.append(VegList.text)
print(NewList)

originalList = NewList.copy() # Copying the original value of NewList in OriginalList
# Then we apply sorting on NewList 
print(originalList)
NewList.sort() # sorting

print(NewList)
print(originalList)
assert NewList == originalList


# vedio 60



# Click on cloumn header
# Collect all veg name in List -> VegList
# Sort this Veg -> NewList
#  VegList == NewList


# In Console
# also we can check the path
# $x("give the locators")








