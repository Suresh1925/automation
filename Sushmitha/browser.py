import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("D:/Sushmitha/framework/python_basics/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.google.com/search?q=nature+images+hd&rlz=1C1CHBF_enIN1021IN1021&oq=nature&aqs=chrome.4.69i57j0i433i512j0i512j0i433i512l5j0i433j0i433i512.9940j0j15&sourceid=chrome&ie=UTF-8")
time.sleep(3)
print("current webpage is ", driver.title)
print("current url is ", driver.current_url)
driver.get("https://www.google.com/search?q=nature+images+hd&rlz=1C1CHBF_enIN1021IN1021&hl=en&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjjxaH35vr6AhUo7XMBHTfxCJIQ_AUoAXoECAMQAw&biw=1536&bih=754&dpr=1.25")
driver.back()
time.sleep(1)
driver.forward()
driver.refresh()
time.sleep(1)
driver.minimize_window()
time.sleep(3)
driver.close()
