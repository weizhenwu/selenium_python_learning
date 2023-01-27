from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

service_obj = Service("../chromedriver")
driver = webdriver.Chrome(service=service_obj)

# opening practise page
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

# find link and click
driver.find_element(By.CSS_SELECTOR, "a[class='blinkingText']").click()

# switch to newly opened tab
# get all opening window tabs. it will return a list contain all tab opened, then switch to the new tab
open_tabs = driver.window_handles
driver.switch_to.window(open_tabs[1])

# explicit wait for the text loaded
waiter = WebDriverWait(driver, 10)
input_text = waiter.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".red"))).text
input_text = input_text.split("at")[1].strip().split(" ")[0]
# close new opened tab
driver.close()
# switch back to origin tab
driver.switch_to.window(open_tabs[0])

# input username and password
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(input_text)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")

# select admin as user type
user_options = Select(driver.find_element(By.CSS_SELECTOR, "select[class='form-control']"))
user_options.select_by_index(1)

# click sign in
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
waiter = WebDriverWait(driver, 10)
alert = waiter.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-danger col-md-12']")))
print(alert.text)
driver.close()
