import time
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

#alerts
#confirm
#radiobutton
#static dropdown
#dynamic dropdown

service_obj = Service("D:/Sushmitha/framework/python_basics/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

name = 'JERRY'
driver.find_element(By.XPATH, '//*[@class="inputs"]').send_keys(name)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="alertbtn"]').click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
time.sleep(3)
alert.accept()     #clicks ok button
time.sleep(3)

name1 = 'TOM'
driver.find_element(By.XPATH, '//*[@class="inputs"]').send_keys(name1)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="confirmbtn"]').click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name1 in alertText
time.sleep(3)
alert.dismiss()     #clicks cancel button
time.sleep(3)


radiobuttons = driver.find_elements(By.XPATH, '//*[@class="radioButton"]')
radiobuttons[2].click()
time.sleep(3)

dropdown = Select(driver.find_element(By.XPATH, '//*[@id="dropdown-class-example"]'))
dropdown.select_by_index(1)
time.sleep(2)
dropdown.select_by_visible_text('Option3')
time.sleep(2)

driver.find_element(By.XPATH, '//*[@class="inputs ui-autocomplete-input"]').send_keys('in')
time.sleep(2)
places = driver.find_elements(By.XPATH, '//*[@class="ui-menu-item"]/div')
print("no of places: ", len(places))
for myplace in places:
    if myplace.text == "India":
        myplace.click()
        break

time.sleep(5)

driver.close()