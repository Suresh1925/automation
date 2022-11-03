# from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
from selenium.webdriver.common.by import By
import time
#service is a class
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)

name = "GCIT"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
# to switch driver mode to alert mode
# by this we can the read the text from alert
alert = driver.switch_to.alert
alertText = alert.text # to grab the alert text into alertText
print(alertText)

assert name in alertText # to conform whether the text is in alert
time.sleep(1) 
alert.accept() # to accept the alert message
# alert.dismiss() # to dismiss the alert message

time.sleep(2) 



