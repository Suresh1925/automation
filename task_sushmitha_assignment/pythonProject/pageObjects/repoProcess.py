from selenium.webdriver.common.by import By


class Repo_Process:
    def __init__(self, driver):
        self.driver = driver

    create_repo_btn = (By.XPATH, '//*[@class="btn btn-sm btn-primary btn mb-2"]')
    na


    def create_repo(self):
        return self.driver.find_element(*Repo_Process.create_repo_btn).click()



