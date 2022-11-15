from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
from selenium.webdriver.common.by import By
import time
#service is a class
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# time.sleep(5)
# driver.find_element(By.ID,"autosuggest").send_keys("ind")
# time.sleep(2)
# # driver.find_element(By.CSS_SELECTOR,"input[class='inputs ui-autocomplete-input valid']").send_keys("del")
# # time.sleep(2)
# countries =driver.find_elements(By.CSS_SELECTOR, "p[class*='blackText']")
# print(len(countries))
# # for country in countries:
# #     if countries.text =="India":
# #         countries.click()
# #         break


# # driver.find_element(By.XPATH,"//p[text()='Delhi, India']").click()
# #vedio 41

# # print(driver.find_element(By.ID,"autosuggest").text)
# assert print(driver.find_element(By.ID,"autosuggest").get_attribute("value")) == "India"

# *******************************

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@class='inputs ui-autocomplete-input']").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.XPATH,"//*[@class='ui-menu-item-wrapper']")  # //*[@class='ui-menu-item']/div
time.sleep(2)
# countries =driver.find_elements(By.CSS_SELECTOR, "p[class*='blackText']")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break


# driver.find_element(By.XPATH,"//p[text()='Delhi, India']").click()
#vedio 41

# print(driver.find_element(By.ID,"autosuggest").text)
assert print(driver.find_element(By.ID,"autosuggest").get_attribute("value")) == "India"





