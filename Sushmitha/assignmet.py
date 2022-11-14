import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("D:/Sushmitha/framework/python_basics/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@class="search-keyword"]').send_keys('c')
time.sleep(2)
order = ['Brocolli - 1 Kg', 'Cauliflower - 1 Kg', 'Cucumber - 1 Kg', 'Carrot - 1 Kg', 'Capsicum', 'Corn - 1 Kg', 'Cashews - 1 Kg']
output = driver.find_elements(By.XPATH, '//*[@class="products"]/div')
count = len(output)
print('no of items found is ', count)
assert count > 0
item = []
for results in output:
    list = results.find_element(By.XPATH, 'h4').text
    item.append(list)

assert order == item
print('items got ', item)

driver.close()