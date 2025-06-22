from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# Setup Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# Open Facebook
driver.get("https://www.facebook.com")
driver.maximize_window()
# Get and print page title and URL
print("Page Title:", driver.title)
print("Page URL:", driver.current_url)
# Interact with elements
txtUserName = driver.find_element(By.ID, "email")
txtUserName.send_keys("abc@gmail.com")
txtPassword = driver.find_element(By.NAME, "pass")
txtPassword.send_keys("123456")
btnLogin = driver.find_element(By.NAME, "login")
btnLogin.click()
OUTPUT :
Page Title: Facebook – log in or sign up
Page URL:  https://www.facebook.com/
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
# Locate and enter email
txtMail = driver.find_element(By.XPATH, "//input[@type='email']")
txtMail.send_keys("abc@gmail.com")
# Locate and enter First Name
txtFst = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
txtFst.send_keys("Azar")
# Locate and enter Last Name
txtLst = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
txtLst.send_keys("AR")
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://facebook.com")
driver.maximize_window()
txtMail = driver.find_element(By.ID, "email")
txtMail.send_keys("abc@gmail.com")
mail = txtMail.get_attribute("value")
print(mail)  ----->  abc@gmail.com
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://greenstech.in/selenium-course-content.html")
driver.maximize_window()
txtAdd = driver.find_element(By.XPATH, "//h6[contains(text(),'Greens')]");
text = txtAdd.text
print(text)
txtAdd1 = driver.find_element(By.XPATH, "//p[@class='mail-info']")
text2 = txtAdd1.text
print(text2)
C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PythonProject4\Selenium\waits.py 
Greens Technology Adyar
No:11,
First Street,
padmanabha Nagar,
Adyar,
Chennai-600 020.
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.shopclues.com/wholesale.html")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)
# Wait for the menu item to appear
sport = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Sports')]")))
actions.move_to_element(sport).perform()
# Wait for submenu and click
weight = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Weight Gainers']")))
weight.click()
**************************************************************************************
import time

from argparse import Action
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
txtMail = driver.find_element(By.XPATH, "//input[@type='email']")
txtMail.send_keys("abc@gmail.com")
txtFst = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
txtFst.send_keys("abc")
txtLst = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
txtLst.send_keys("abc123")
mail = txtMail.get_attribute("value")
print(mail)
C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PythonProject4\Selenium\waits.py 
abc@gmail.com
**************************************************************************************

**************************************************************************************

**************************************************************************************
**************************************************************************************

**************************************************************************************
**************************************************************************************

**************************************************************************************
**************************************************************************************
**************************************************************************************

**************************************************************************************
**************************************************************************************

**************************************************************************************
**************************************************************************************

**************************************************************************************
**************************************************************************************

**************************************************************************************
