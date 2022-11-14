from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
#service is a class
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # get is a method 
print(driver.title) # to get tab title of web browser 
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/")
# driver.minimize_window
driver.back()
driver.refresh()
# driver.forward()




driver.close() # close is a method which is used to close the browser 