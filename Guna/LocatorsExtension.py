from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:/User2/Python-Automation/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://login.salesforce.com/")
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Rahul")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("shetty")
driver.find_element(By.XPATH, "//input[@id='password']").clear()
driver.find_element(By.XPATH, "//a[@id='forgot_password_link']").click()
#//tagname[text()=’xxx’]
driver.find_element(By.XPATH,"//input[@type='button']").click()
print(driver.find_element(By.XPATH,"//form[@name='login']/div[1]/label").text)
#print(driver.find_element(By.CSS_SELECTOR , ("form[name='login'] label:nth-child(3)").text))





