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
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
act = ActionChains(driver)
driver.get("https://greenstech.in/selenium-course-content.html")
driver.maximize_window()
txtAdd = driver.find_element(By.XPATH, "//h6[contains(text(), 'Greens')]")
text1 = txtAdd.text
print(text1)
txtMail = driver.find_element(By.XPATH, "//p[@class='mail-info']")
text2 = txtMail.text
print(text2)
time.sleep(10)
act.move_to_element(txtAdd).perform()
time.sleep(10)
OUTPUT:--------------
Greens Technology Adyar
No:11,
First Street,
padmanabha Nagar,
Adyar,
Chennai-600 020.
**************************************************************************************
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demo.guru99.com/test/drag_drop.html")
act = ActionChains(driver)
sour1 = driver.find_element(By.XPATH, "//a[text()=' BANK ']")
dest1 = driver.find_element(By.XPATH, "(//li[@class='placeholder'])[1]")
act.drag_and_drop(sour1, dest1).perform()
time.sleep(10)
sour2 = driver.find_element(By.XPATH, "//a[text()=' 5000 ']")
dest2 = driver.find_element(By.ID, "amt7")
act.drag_and_drop(sour2, dest2).perform()
**************************************************************************************
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# Set up Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# Load the webpage
driver.get("https://www.greenstechnologys.com/")
time.sleep(3)
# Find a paragraph and perform double-click and right-click
paragraph = driver.find_element(By.XPATH, "//p[contains(@style, 'font-size: 18px')]")
act = ActionChains(driver)
act.double_click(paragraph).perform()
act.context_click(paragraph).perform()
time.sleep(2)
# Use keyboard to navigate context menu
pyautogui.keyDown('down')
time.sleep(0.5)
pyautogui.keyUp('down')
# Press Enter
pyautogui.press('enter')  # OR:
# pyautogui.keyDown('enter')
# pyautogui.keyUp('enter')
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.find_element(By.XPATH, "//button[@onclick='alertbox()']").click()
alert = driver.switch_to.alert
alert.accept()
**************************************************************************************
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Alert with Textbox')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@onclick='promptbox()']").click()
time.sleep(2)
pyautogui.typewrite("abc")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)
output = driver.find_element(By.ID, "demo1").text
print("Alert result on page:", output)
driver.quit()
**************************************************************************************
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.facebook.com")
time.sleep(2)
email_field = driver.find_element(By.ID, "email")
driver.execute_script("arguments[0].setAttribute('value','testuser@example.com');", email_field)
value = driver.execute_script("return arguments[0].getAttribute('value')", email_field)
print("Email field value is:", value)
txtpass = driver.find_element(By.ID, "pass")
driver.execute_script("arguments[0].setAttribute('value','12345');", txtpass)
btnLogin = driver.find_element(By.NAME, "login")
driver.execute_script("arguments[0].click();", btnLogin)
time.sleep(3)
driver.quit()
**************************************************************************************
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://toolsqa.com")
time.sleep(2)
try:
    driver.find_element(By.ID, "cookie_action_close_header").click()
    time.sleep(1)
except:
    pass
txtScroll = driver.find_element(By.XPATH, "//div[text()='Selenium Online Trainings']")
driver.execute_script("arguments[0].scrollIntoView(false);", txtScroll)
time.sleep(3)
driver.execute_script("arguments[0].scrollIntoView(true);", txtScroll)
time.sleep(3)
driver.quit()
**************************************************************************************
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://toolsqa.com")
time.sleep(2)
try:
    driver.find_element(By.ID, "cookie_action_close_header").click()
    time.sleep(1)
except:
    pass
txtScroll = driver.find_element(By.XPATH, "//div[text()='Selenium Online Trainings']")
driver.execute_script("arguments[0].scrollIntoView(false);", txtScroll)
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView(true);", txtScroll)
driver.save_screenshot("selenium_training_section.png")
print("Screenshot saved as selenium_training_section.png")
driver.quit()
**************************************************************************************
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://toolsqa.com")
try:
    driver.find_element(By.ID, "cookie_action_close_header").click()
    time.sleep(1)
except:
    pass
txtScroll = driver.find_element(By.XPATH, "//div[text()='Selenium Online Trainings']")
driver.execute_script("arguments[0].scrollIntoView(false);", txtScroll)
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView(true);", txtScroll)
time.sleep(1)
pyautogui.screenshot("selenium_training_section1.png")
driver.quit()
**************************************************************************************
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.facebook.com")
btnLogin = driver.find_element(By.NAME, "login")
displayed = btnLogin.is_displayed()
print(displayed)
enabled = btnLogin.is_enabled()
print(enabled)
btnCreate = driver.find_element(By.XPATH, "//a[text()='Create new account']")
btnCreate.click()
rdoGender = driver.find_element(By.NAME, "sex")
rdoGender.click()
selected = rdoGender.is_selected()
print(selected)
driver.quit()
**************************************************************************************

**************************************************************************************
**************************************************************************************

**************************************************************************************
**************************************************************************************

**************************************************************************************
