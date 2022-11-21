from selenium.webdriver.common.by import By

from pageObjects.logoutPage import LogoutPage


# from pageObjects.confirm import Confirm


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    user_name_text_box_xpath = (By.XPATH, '//*[@class="form-control input-block js-login-field"]' )
    password_text_box_xpath = (By.XPATH, '//*[@class="form-control form-control input-block js-password-field"]')
    submit_button_xpath = (By.XPATH, '//*[@class="btn btn-primary btn-block js-sign-in-button"]')


    def username(self):
        # self.driver.find_element(self.user_name_text_box_xpath).clear
        return self.driver.find_element(*LoginPage.user_name_text_box_xpath).send_keys("sushmitha.srinivasan@gcitsolutions.com")

    def password(self):
        return self.driver.find_element(*LoginPage.password_text_box_xpath).send_keys("akilaa01062000s")

    def submit(self):
        self.driver.find_element(*LoginPage.submit_button_xpath).click()
        logoutPage = LogoutPage(self.driver)
        return logoutPage




