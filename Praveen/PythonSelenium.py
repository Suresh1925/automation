from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\\Users\Praveen\PycharmProjects\PraveenProject\driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://flipkart.com")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
