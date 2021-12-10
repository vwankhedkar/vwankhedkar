from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Selenium\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
print(driver.find_element_by_tag_name("h3").text)
driver.find_element_by_link_text("Click Here").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.find_element_by_tag_name("h3").text)
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)


