from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

opt = Options()
opt.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path=r"D:\Selenium\chromedriver.exe",options=opt)
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
driver.maximize_window()
action.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
