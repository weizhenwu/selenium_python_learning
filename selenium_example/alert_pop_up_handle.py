from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("../chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys("demo name")
driver.find_element(By.ID, "alertbtn").click()

# switch to pop up alert
alert = driver.switch_to.alert
alertText = alert.text
assert "demo name"  in alertText, "Name is not correct!"

# click on alert's button
alert.dismiss()

# dismiss = cancel (negative), accept = ok (postive)
driver.find_element(By.ID, "alertbtn").click()
alert.accept()
