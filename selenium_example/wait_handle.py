from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# for locater
from selenium.webdriver.common.by import By
# for tag = select
from selenium.webdriver.support.select import Select
# for explicit wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service("/home/weichenwu/selenium_learning/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# impliciit wait means, when driver try to find a element, it will wait at max 5 seconds for the element to load
# if the element loaded less than 5 seconds, it will end waiting right away
# but this is not applied to find_elements, since find_elements will return empty list [] if it cannot find any.
# [] is still a valid return, so it will be considerated as elements found. which will end waiting right away
driver.implicitly_wait(3)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.CSS_SELECTOR, "div[class='product']")
desired_product_names = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
product_names = []

for product in products:
    product_names.append(product.find_element(By.CSS_SELECTOR, ".product-name").text)
    # web element changing, find element in current block
    product.find_element(By.CSS_SELECTOR, "button").click()
assert desired_product_names == product_names, "Not match!"

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# explicit wait means, it will only appled to given condition in case some actions take more than average time applied to imlicity wait
# 10 seconds for this example
# explicit -> applied for specific condition, implicit -> globle wait time
wait = WebDriverWait(driver, 10)
text = wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo"))).text
assert text == "Code applied ..!", "failed!"

# check amount
amounts = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(5) p[class='amount']")
total = sum(int(amount.text) for amount in amounts)
actual_total = int(driver.find_element(By.CSS_SELECTOR, "span[class='totAmt']").text)
assert total == actual_total, "Not Match!"
discount_total = float(driver.find_element(By.CSS_SELECTOR, "span[class='discountAmt']").text)
assert discount_total < actual_total, "Discount is not applied!"
