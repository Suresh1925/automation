from time import time
#from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
#service is a class
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/") # get is a method 
time.sleep(10)
# locators - ID, Xpath, CSS selector, class name, name, linktext
driver.find_element(By.NAME,"email").send_keys("hello@123.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("xsedfc")


# Xpath = //tagname[@attribute="value"] -> e.g: //input[@type='submit'] 
# CSS = tagname[attribute="value"] -> e.g: input[type='submit'] 
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Keerthana")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

# Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
#dropdown.select_by_value()

driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click() #for radio button
message = driver.find_element(By.CLASS_NAME,"alert-success").text # text = to grab the text
print(message)
assert "Success" in message # will check the string in message variable
# if condition True, returns nothing
# if condition False returns AssertionError

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hi")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear() # to clear the data 



time.sleep(5)

driver.close() # close is a method which is used to close the browser 