from selenium import webdriver
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Johnbabu/PycharmProjects/pythonProject/Driver/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://nadsiadlvelysdsperadl.z13.web.core.windows.net/")
driver.fullscreen_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "//button[@class='buttonStatus' and text()='Deltachange']").click()
# driver.find_element(By.XPATH, "//input[@placeholder='enter epoch']").click()
driver.find_element(By.XPATH, "//input[@value='5 mins']").click()
driver.find_element(By.XPATH, "//input[@value='5 mins']").click()





# driver.find_element(By.XPATH, "//button[@class='buttonStatus' and text()='Deltachange']").click()
# driver.find_element(By.XPATH, "//input[@placeholder='enter dsep patient id']").click()
# with open("text.txt", "r") as reader:
#     rev = reader.read()
#     print(rev)
# driver.find_element(By.XPATH, "//input[@placeholder='enter dsep patient id']").send_keys(rev)
driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and text()='send']").click()
