
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object #service is a class
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
service_obj = Service("C:\\Users\Praveen\PycharmProjects\PraveenProject\driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR , "a[href*= 'shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products :
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.CSS_SELECTOR,"button[class*='btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
#wait = webDriverWait(driver,10)
#wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT,"India"))
time.sleep(5)
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
successText = driver.find_elements(By.CLASS_NAME,"alert-dismissible").text
assert "Success! Thank You!" in successText
driver.close()
