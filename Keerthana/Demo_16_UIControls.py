from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
from selenium.webdriver.common.by import By
import time
#service is a class
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
# when values are chaning in list
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
time.sleep(2)
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value")  == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

# when position will cahnge use for loop
# when position is constant, use index directly
radiobuttons = driver.find_element(By.XPATH,"(//input[@class='radioButton'])[2]") #
radiobuttons.click()
assert radiobuttons.is_selected()

assert driver.find_element(By.ID,"//input[@id='displayed-text']").is_displayed() #before hiding
driver.find_element(By.ID,"//input[@id='hide-textbox']").click()
assert not driver.find_element(By.ID,"//input[@id='displayed-text']").is_displayed() # after hiding







