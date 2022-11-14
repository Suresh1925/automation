from ssl import Options
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object #service is a class
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Chrome Option 
# To learn : https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")# certification error

# to connect chrome option to actual 
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe") 
driver = webdriver.Chrome(service=service_obj, options=chrome_option)# actual invocation

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)










