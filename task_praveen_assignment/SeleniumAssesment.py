import time
from selenium import webdriver
from selenium.webdriver import ActionChains
#chromedriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
service_obj = Service("C:\\Users\Praveen\PycharmProjects\PraveenProject\driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

def test_login():
    driver.find_element(By.XPATH, "//input[@class='input_error form_input']").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

def test_Dropdown():
    dropdown = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
    dropdown.select_by_visible_text("Name (A to Z)")
    time.sleep(2)
    #wait = WebDriverWait(driver, 10)

def test_addtocart():
    results = driver.find_elements(By.XPATH, "//div[@class='inventory_item']")
    resultsName =driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
    time.sleep(2)
    #resultsName = driver.find_elements(By.XPATH, "//div[@class='inventory_item_description']")
    AddToCart = driver.find_elements(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")
    for i in range(0,len(resultsName)):
        print(resultsName[i].text)
        if "Sauce" in resultsName[i].text:
            AddToCart[i].click()
    time.sleep(2)

def test_Checkout():
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.XPATH, "// button[text() = 'Checkout']").click()
    time.sleep(2)
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.ID,"first-name"))).send_keys("Praveen")
    driver.find_element(By.ID,"last-name").send_keys("Anbuchezhian")
    driver.find_element(By.ID, "postal-code").send_keys(600005)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@class='btn btn_action btn_medium cart_button']").click()
    time.sleep(2)

def test_Exception():
    ItemsInCart = 5
    if ItemsInCart != 5:
        raise Exception("Product in the cart count matches")

def test_Assertion():
    #driver.save_screenshot("Success.png")
    assert driver.find_element(By.XPATH, "//h2[@class='complete-header']").text == "THANK YOU FOR YOUR ORDER"







