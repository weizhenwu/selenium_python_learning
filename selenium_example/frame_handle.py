from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("../chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

# frame is an embedding html page in current html page, so we need to switch_to the embeded page first
driver.switch_to.frame("mce_0_ifr")
print(driver.find_element(By.CSS_SELECTOR, "body[id='tinymce'] p").text)

# switch back
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
