from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object #service is a class
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(2)

driver.find_element(By.XPATH,"//a[@class='nav-link' and text()='Shop']").click() # CSS = a[href*='shop'] (* is used to give partial value)
# xpath = //a[contains(@href,'shop')]

# windowsopened = driver.window_handles
# driver.switch_to.window(windowsopened[1])
mobiles = driver.find_elements(By.XPATH,"//h4[@class='card-title']")

# here we can use chanining concept also

for mobile in mobiles:
    mobile.text
    if mobile == "Nokia Edge":
        driver.find_element(By.XPATH,"(//button[@class='btn btn-info'])[3]").click()
        break


driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()

# driver.switch_to.window(windowsopened[2])

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10) # 2 arg, driver object and how many sec to wait
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-success btn-lg']").click()

text = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in text # to check the partial text present use "in" keyword
 


# driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()



