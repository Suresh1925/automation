import time
import pytest as pytest
import selenium
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver =selenium.webdriver.Chrome(executable_path="C:\\Users\Praveen\PycharmProjects\PraveenProject\driver\chromedriver.exe")
    elif browser_name == "edge":
        driver =selenium.webdriver.Edge(executable_path="D:/Sushmitha/framework/python_basics/driver/msedgedriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


