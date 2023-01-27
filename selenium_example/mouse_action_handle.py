from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# for locater
from selenium.webdriver.common.by import By
# for mouse action
from selenium.webdriver import ActionChains

service_obj = Service("../chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# for handling user perfoming actions, we have ActionChains in selenium
action = ActionChains(driver)

# start to build ActionChains quene
action.move_to_element(driver.find_element(By.ID, "mousehover"))
# context_click means right click
action.context_click(driver.find_element(By.XPATH, "//a[text()='Reload']"))
action.scroll_to_element(driver.find_element(By.ID, "mousehover"))

# after added actions to ActionChains quene, call perform to actually execute those actions
# also can add .perform() after every action above instead of calling it at the end
action.perform()
