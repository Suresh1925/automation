from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("E:/User2/Python-Automation/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe",options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)