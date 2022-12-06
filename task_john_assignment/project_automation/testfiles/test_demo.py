from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import json
import time


with open("../test_data/testdata.json") as jsonFile:    #Loading testdata
    jsonObject = json.load(jsonFile)
    jsonFile.close()



service_object = Service("C:/Users/Johnbabu/PycharmProjects/project_automation/Drivers/chromedriver.exe")

driver = webdriver.Chrome(service=service_object)
driver.maximize_window()

driver.get(jsonObject["url"])

driver.implicitly_wait(5)   #implicit wait




def test_portal_login():

        driver.refresh()
        time.sleep(2)   #sleep
        driver.find_element(By.XPATH, "(//li[@class='authorization-link']//a)[1]").click()
        # driver.e_wait(5)
        driver.find_element(By.XPATH, "(//input[@type='email'])[1]").send_keys(jsonObject["username"])
        driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys(jsonObject["password"])
        driver.find_element(By.XPATH, "(//button[@id='send2'])[1]").click()
        driver.find_element(By.XPATH, "//input[@placeholder ='Search entire store here...']").send_keys(jsonObject["dress"])
        driver.find_element(By.XPATH, "//button[@title='Search']").click()
        totals = driver.find_elements(By.XPATH, "//div[@class='product details product-item-details']//strong//a")  #Loading webelemets

        try:
                for total in totals:
                        # print(total.text)
                        if total.text == jsonObject["dresstype"]:
                                assert total.text == jsonObject["dresstype"]
                                driver.find_element(By.XPATH, "(//li[@class='item product product-item']//a[@href='https://magento.softwaretestingboard.com/diva-gym-tee.html'])[2]").click()
                                driver.find_element(By.XPATH, "//div[@option-label='Orange']").click()
        except Exception as e:
                print(e)

        # driver.close()



