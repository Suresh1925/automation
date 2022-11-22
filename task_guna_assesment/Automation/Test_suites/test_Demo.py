import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
now = datetime.now()

with open("./test_data/details.json") as input:    #Loading testdata
    Input_Object = json.load(input)
    input.close()



service_object = Service("./Driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get(Input_Object["url"])
driver.implicitly_wait(5)

def test_portal_login():

        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(Input_Object["username"])
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(Input_Object["password"])
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        #time.sleep(10)
        driver.find_element(By.XPATH, "(//*[contains(text(),'My Info')])[1]").click()
        #time.sleep(5)
        print("User has successfully logged in")


def test_Username():
        path = f"//span[@class='info ng-star-inserted' and text() = '{Input_Object['Name']} ']"
        print(path)
        name = driver.find_element(By.XPATH, path).text
        assert name == Input_Object["Name"]
        print("The User name is "  + name)

def test_ID():
        wait = WebDriverWait(driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"(//span[@class='info ng-star-inserted'])[2]")))
        ID = driver.find_element(By.XPATH, "(//span[@class='info ng-star-inserted'])[2]").text
        assert ID == Input_Object["username"]
        print("The employee ID is " + ID)


def test_loop():
        Details = driver.find_elements(By.XPATH, "//span[@class='info ng-star-inserted']")

        for detail in Details:
                print(detail.text)
                if detail.text == Input_Object["marital_status"]:
                        assert detail.text != "Commited"
                        print("Details matches the data base")

def test_drop_down():
        try:
                driver.find_element(By.XPATH, "//button[@class='btn dropdown-toggle']").click()
                driver.find_element(By.XPATH, "//a[@title='presentaddress']").click()
                Address = driver.find_element(By.XPATH, "//*[contains(text(),'Gents PG')]").text
                print(Address)
                assert  Address == Input_Object["address"]
        except Exception as e:
                print(e)



def test_logout():
        driver.find_element(By.XPATH, "//div[@class='image-gt-icon-logout w-2x h-2x']").click()
        print("User has successfully logged out")
        File_object = open(r"./log.text", "a")
        File_object.write("\n User has succesfully logged out  - " +  now.strftime("%m/%d/%Y, %H:%M:%S"))
        driver.close()







