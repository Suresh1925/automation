import time

from selenium import webdriver
from selenium.webdriver import Keys

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("E:/User2/Python-Automation/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#driver.get("http://demo.guru99.com/test/selenium-xpath.html")
driver.get("https://www.flipkart.com/")
"//h4/a[contains(text(),'SAP M')]"
# ID, Xpath, CSSSelector, Classname, name, linkText
#driver.find_element(By.XPATH,"(//input[@class='_2IX_2- VJZDxU'])").send_keys("7708486542")