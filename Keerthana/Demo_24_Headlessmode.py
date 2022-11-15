# from pickletools import optimize
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
from selenium.webdriver.common.by import By
import time 
from io import StringIO
from PIL import Image

# Headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

# When there is message like "Praivate page" or button to be clicked like "Advance", 
# or to ignore all the certification error
# for driver to handle it automatically we use the following
chrome_options.add_argument("--ignore-certificatr-errors")

service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj , options=chrome_options) # integrating browser before invoking

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(2)

# To scroll
# Go to console after inspect
# window.scroll(0,500) -> to scroll from 0 to 500 pixcel of the page
# window.scroll(0,document.body.scrollHeight) -> to scroll from 0 to end of the page

driver.execute_script("window.scroll(0,document.body.scrollHeight);") # execute_script means Java script
driver.get_screenshot_as_file("screen.png")

# screenshot = driver.get_screenshot_as_png()
# size = (0,0,60,400)
# image = Image.open(StringIO.stringIO(screenshot))
# region = image.crop(size)
# region.save('sample_screenshot_3.jpg', 'JEPG', optimize=True, quality = 95)

# Head mode
# We can see the actual action. Browser opens and see actual action
# Headless mode
# We can't see the actual action. Browser opens in back end and cant see actual action
# test will run in invisible mode





