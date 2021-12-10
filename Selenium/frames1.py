from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\Selenium\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/tinymce")
driver.switch_to.frame("mce_0_ifr")
wait = WebDriverWait(driver, 10)
onFrame = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'#tinymce')))
onFrame.click()
onFrame.clear()
driver.find_element_by_css_selector("body[id='tinymce']").send_keys("Writing in tinymce")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
