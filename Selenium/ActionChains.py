import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.sbilife.co.in/")
menu = driver.find_elements(By.XPATH, "//div[@id='container']/div[2]/ul/li")
action = ActionChains(driver)
for item in menu[0:5]:
    action.move_to_element(item).perform()
    time.sleep(5)
action.move_to_element(menu[0]).perform()
child = driver.find_element(By.LINK_TEXT,"Learn About Insurance")
action.move_to_element(child).click().perform()
