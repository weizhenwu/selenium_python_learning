from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
# start browser maximized
chrome_options.add_argument("--start-maximized")
# don't open a actual browser, run in backround
chrome_options.add_argument("headless")
# ignore SSL certificate
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("../chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
