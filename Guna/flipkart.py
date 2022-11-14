import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("E:/User2/Python-Automation/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.flipkart.com/")
driver.maximize_window()

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.XPATH,"(//input[@class='_2IX_2- VJZDxU'])").send_keys("7708486542")
driver.find_element(By.XPATH, "(//input[@class='_2IX_2- _3mctLh VJZDxU'])").send_keys("Flipkartlogin")
#driver.close()
driver.find_element(By.XPATH, "(//button[@class='_2KpZ6l _2HKlqd _3AWRsL'])").click()
time.sleep(10)
#driver.find_element(By.XPATH, "(//button[@class='_2KpZ6l _2HKlqd _3AWRsL'])").click()
#driver.find_element(By.XPATH, "(//input[@class='_3704LK'])").send_keys("Realme")
#driver.find_element(By.XPATH, "(//input[@class='_3704LK'])").clear
driver.find_element(By.XPATH, "//input[@class='_3704LK']").send_keys("Realme x7")
driver.find_element(By.XPATH, "(//button[@type='submit'])").send_keys(Keys.ENTER)
time.sleep(10)
models = driver.find_elements(By.XPATH, "(//div[@class='_2kHMtA'])")
for model in models :
    model.text == "realme X7 5G (Space Silver, 128 GB)"
    model.click()
    break
Childwindow = driver.window_handles
driver.switch_to.window(Childwindow[1])
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//a[@class = '_1fGeJ5']")).perform()

