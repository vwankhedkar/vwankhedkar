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

**************************************************************************************
**************************************************************************************

**************************************************************************************
**************************************************************************************

**************************************************************************************
**************************************************************************************

**************************************************************************************
**************************************************************************************

**************************************************************************************
