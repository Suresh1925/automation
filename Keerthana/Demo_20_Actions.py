from selenium import webdriver
from selenium.webdriver.chrome.service import Service #here service is a object
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
service_obj = Service("D:\Automation\Selenium_Python_Udemy\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(2)

# For Mouse over
# ActionChains is class and we have to pass driver as an argument
action = ActionChains(driver) # action is variable created 
#action.context_click() # context is right clicking
#action.click_and_hold(path of the element)
#action.double_click
#action.drag_and_drop(source of the path, detination element path)
#action.move_to_element() # it will just move to the web element

action.move_to_element(driver.find_element(By.XPATH,"//button[@id='mousehover']")).perform()
# all the action method should end with .perform then only the action will be executed
time.sleep(1)
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
#action.context_click(driver.find_element(By.XPATH,"//a[text()='Top']")).perform()
time.sleep(2)
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
# can perform send keys operation in action class




