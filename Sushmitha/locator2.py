import time
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


#show/hide button
#checkbox

service_obj = Service("D:/Sushmitha/framework/python_basics/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("file:///D:/Sushmitha/Daily_regression_dsp_daa_fhir_layering/dsp_daa_fhir_layering/HtmlReport/history/DocsperaEHR_Report_dev_09-01-2022/DocsperaEHR_Report_dev_09-01-2022(error).html")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@href="javascript:hideAllExtras()"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@href="javascript:showAllExtras()"]').click()
time.sleep(2)

checkboxes = driver.find_elements(By.XPATH, '//*[@type="checkbox"]')
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("data-test-result") == "failed":
        checkbox.click()
        try:
            checkbox.is_selected()
            print("failed checkbox is not selected")
        except:
            print("failed checkbox is selected")

        break
time.sleep(3)


driver.close()