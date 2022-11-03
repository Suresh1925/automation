from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object #service is a class
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.implicitly_wait(2) # driver will wait for maximum 5s, if it finds the element in 2s, it will proceed
# This implicit wait is global, wherever driver is taking time to find element it will wait

driver.find_element(By.XPATH,"//*[@class='search-keyword']").send_keys("be")
time.sleep(2) # here we need sleep inspight of implicit bez 
#even when the list is empty, implicit thinks we got result so it will continue to next 
results = driver.find_elements(By.XPATH,"//div[@class='product']") # returns list of values
print(len(results))
count = len(results)
assert count > 0

# Assignment 2 
ExpectedList = [ "Cucumber - 1 Kg", "Beetroot - 1 Kg", "Beans - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []
# Chaining of web elements
for result in results:
    # actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click() 
    # Chaining. The result holds the path, we are chaining/ adding to that path
# assert ExpectedList == actualList

# Assignment 2
listVegs = driver.find_elements(By.XPATH,"//h4[@class='product-name']")
Veg = []

for listVeg in listVegs:
    Veg.append(listVeg.text)
print(Veg)
assert ExpectedList == Veg


driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

# Sum vadlidation
prices = driver.find_elements(By.XPATH,"//td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)

totalAmt = int(driver.find_element(By.XPATH,"//span[@class='totAmt']").text)

assert sum == totalAmt

driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()

wait = WebDriverWait(driver,10) # 2 arg, driver object and how many sec to wait
# explicit wait, particularly wait for the particular line to fetch/execute 
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[text()='Code applied ..!']"))) #wait is given here

print(driver.find_element(By.XPATH,"//span[text()='Code applied ..!']").text)


# Assignment 1
discountAmt = float(driver.find_element(By.XPATH,"//span[@class='discountAmt']").text)

assert totalAmt > discountAmt






