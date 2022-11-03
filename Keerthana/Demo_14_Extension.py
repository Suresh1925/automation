from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
from selenium.webdriver.common.by import By
import time
#service is a class
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/client") # get is a method  ## 
time.sleep(5)
# locators - ID, Xpath, CSS selector, class name, name, linktext
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
time.sleep(5)
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com") #Xpath to travel from parent to child class
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@12345") #CSS to travel from parent to child class # in CSS use space instead of /
# Xpath - //form/div[2]/input
driver.find_element(By.ID, "confirmPassword").send_keys("Hello@12345")
# driver.find_element(By.XPATH,"//button[@type='submit']").click() 

# locators identifed based on text in webpage
# Syntax = //tagname[text()='give the entire text here']
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
time.sleep(3)

driver.close()