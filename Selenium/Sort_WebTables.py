import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
browserSortedVeggies = []
service_obj = Service("D:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers/")
#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# Collect all veggie names -> BrowserSortedVeggieList (A,B,C)
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
time.sleep(5)
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)
originalBrowserSortedList = browserSortedVeggies.copy()
