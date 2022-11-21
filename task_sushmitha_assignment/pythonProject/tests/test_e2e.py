import time

from pageObjects import logoutPage
from pageObjects.loginPage import LoginPage
from utilities.BaseClass import BaseClass

             ###  if test fails screenshot is taken automatically but it happens only when test fails  ###

class Test_one(BaseClass):
    def test_e2e(self, setup):
        log = self.test_logdemo()
        loginPage = LoginPage(self.driver)
        logoutPage = loginPage.submit()
        time.sleep(2)
        loginPage.username()
        loginPage.password()
        loginPage.submit()
        time.sleep(2)
        logoutPage.clickicon()
        time.sleep(2)
        logoutPage.signout()
        time.sleep(2)



