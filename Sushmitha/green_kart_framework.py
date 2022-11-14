import time
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#waits
#implicite wait - globally applied
#explicite wwait - for special condition & time exceeds more than implicite wait

service_obj = Service("D:/Sushmitha/framework/python_basics/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@class="search-keyword"]').send_keys('c')
time.sleep(2)
output = driver.find_elements(By.XPATH, '//*[@class="products"]/div')
count = len(output)
print(count)
assert count > 0
for results in output:
    results.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.XPATH, '//*[@alt="Cart"]').click()
driver.find_element(By.XPATH, '//*[text()="PROCEED TO CHECKOUT"]').click()

#amount validation
total = int(driver.find_element(By.XPATH, "//*[@class='totAmt']").text)
prices = driver.find_elements(By.XPATH, '//tr/td[5]/p')
sum = 0
for price in prices:
    sum = sum + int(price.text)

print('total sum is ', sum)
assert sum == total

driver.find_element(By.XPATH, '//*[@class="promoCode"]').send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, '//*[@class="promoBtn"]').click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@class="promoCode"]')))
print(driver.find_element(By.XPATH, '//*[@class="promoInfo"]').text)
discountedAmount = float(driver.find_element(By.XPATH, '//*[@class="discountAmt"]').text)
assert  total > discountedAmount
print('amount after discount is ',discountedAmount)
driver.close()