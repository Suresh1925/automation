from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(2)

driver.find_element(By.TAG_NAME, "a").click()

newwindow = driver.window_handles

driver.switch_to.window(newwindow[1])
mailid = driver.find_element(By.XPATH, "//a[text()='mentor@rahulshettyacademy.com']").text
print(mailid)

driver.switch_to.window(newwindow[0])
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(mailid)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("As")
message = driver.find_element(By.XPATH, "//p[@class='text-center text-white']").text
print(message)





# By Rahul

# import time

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait

# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
# driver.implicitly_wait(4)

# driver.get("https://rahulshettyacademy.com/loginpagePractise/")
# driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
# windowsOpened = driver.window_handles

# driver.switch_to.window(windowsOpened[1])
# message = driver.find_element(By.CSS_SELECTOR, ".red").text
# var = message.split("at")[1].strip().split(" ")[0]
# driver.close()
# driver.switch_to.window(windowsOpened[0])
# driver.find_element(By.ID, "username").send_keys(var)
# driver.find_element(By.ID, "password").send_keys(var)
# driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
# wait = WebDriverWait(driver,10)
# wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
# print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)








