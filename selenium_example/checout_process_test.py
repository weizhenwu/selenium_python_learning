from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
service_obj = Service("../chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

# open web and redirect to shop page
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT, "Shop").click()

# find all product cards
products = driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")
for product in products:
    product_name = product.find_element(By.CSS_SELECTOR, "h4 a").text
    # add nokia to checkout cart
    if product_name == "Nokia Edge":
        product.find_element(By.CSS_SELECTOR, "button").click()
        break

# redirect to checkout page
driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

# key in ind to get auto suggesstion
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
wait = WebDriverWait(driver, 10)
suggestion = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='India']")))
suggestion.click()

# click submit and check alert text
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
alert_text = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in alert_text, "Alert text is not correct!"

driver.close()
