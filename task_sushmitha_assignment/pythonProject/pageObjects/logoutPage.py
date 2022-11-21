from selenium.webdriver.common.by import By

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    dropdown_xpath = (By.XPATH, '//*[@class="avatar avatar-small circle"]')
    logout_xpath =(By.XPATH, '//*[@class="dropdown-item dropdown-signout"]')

    def clickicon(self):
        self.driver.find_element(*LogoutPage.dropdown_xpath).click()

    def signout(self):
        self.driver.find_element(*LogoutPage.logout_xpath).click()