from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
service_obj = Service("D:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
