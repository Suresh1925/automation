from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("E:/User2/Python-Automation/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.flipkart.com/")

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.XPATH,"(//input[@class='_2IX_2- VJZDxU'])").send_keys("7708486542")
driver.find_element(By.XPATH, "(//input[@class='_2IX_2- _3mctLh VJZDxU'])").send_keys("Flipkartlogin")
#driver.close()
driver.find_element(By.XPATH, "(//button[@class='_2KpZ6l _2HKlqd _3AWRsL'])").click()
driver.find_element(By.XPATH, "(//input[@class='_3704LK'])").send_keys("Realme x7")
driver.find_element(By.XPATH, "(//input[@class='_3704LK'])").send_keys("ENTER")
# driver.refresh();
# driver.find_element(By.XPATH, "(//button[@class='L0Z3Pu'])").click()