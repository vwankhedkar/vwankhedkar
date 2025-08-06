from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("D:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
# //a[contains(@href,'shop')]  a[href*='shop']
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME,"alert-success").text
print(successText)
assert "Success! Thank you!" in successText
driver.close()
*************************************************************************************
Sorting dropdown
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
dropdown = Select(driver.find_element(By.XPATH, "//select[@id='animals']"))
options = dropdown.options
original_list = []
tmp_list = []
for option in options:
    original_list.append(option.text)
    tmp_list.append(option.text)
print("Before sorting ...")
print("Original List:", original_list)
print("Temp List:", tmp_list)
tmp_list.sort()
# Print both lists
print("After sorting ...")
print("Original List:", original_list)
print("Temp List:", tmp_list)
driver.quit()
