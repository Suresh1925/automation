import time
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkoutPage import CheckoutPage
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass

class Test_one(BaseClass):
    def test_e2e(self, setup):
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        # checkoutPage = CheckoutPage(self.driver)
        products = checkoutPage.getproductTitle()

        for product in products:
            productName = product.find_element(By.XPATH, 'div/h4/a').text
            if productName == "Blackberry":
                product.find_element(By.XPATH, 'div/button').click()
        checkoutPage.clickprimaryButton().click()
        confirmPage = checkoutPage.clicksucessButton()
        confirmPage.getfilterValid().send_keys('ind')
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        confirmPage.linkText().click()
        confirmPage.getcheckbox().click()
        confirmPage.get_btn().click()
        info = confirmPage.alert().text
        assert 'Success!' in info
        print(info)
        self.driver.close()
