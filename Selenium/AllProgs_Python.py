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
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("http://jqueryui.com/resources/demos/droppable/default.html")
drag = driver.find_element(By.XPATH, "//*[@id='draggable']")
drop = driver.find_element(By.XPATH, "//*[@id='droppable']")
act = ActionChains(driver)
act.drag_and_drop(drag, drop).perform()
# # FluentWait using WebDriverWait with polling and ignored exceptions
# wait = WebDriverWait(driver, timeout=20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
#
# # Wait until login button is clickable
# login_button = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
# login_button.click()
**********************************************************************************************
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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.switch_to.frame("login_page")  # Correct frame name
time.sleep(2)
customer_id_input = driver.find_element(By.NAME, "fldLoginUserId")
customer_id_input.send_keys("12345678")  # Use a valid dummy or actual ID
# Step 2: Now click the Continue button
continue_btn = driver.find_element(By.CLASS_NAME, "login-btn")
continue_btn.click()
# Step 3: Switch back to default content (if needed later)
driver.switch_to.default_content()
time.sleep(5)
driver.quit()

**************************************************************************************
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.snapdeal.com")
time.sleep(2)
txtSearch = driver.find_element(By.ID, "inputValEnter")
txtSearch.send_keys("Hand Sanitizer")
btnSearch = driver.find_element(By.XPATH, "//span[text()='Search']")
btnSearch.click()
time.sleep(2)
btnPro = driver.find_element(By.XPATH, "(//img[@class='product-image '])[1]")
btnPro.click()
time.sleep(2)
parentWin = driver.current_window_handle
allWind = driver.window_handles
# Switch to the new window
for win in allWind:
    if win != parentWin:
        driver.switch_to.window(win)
        break
print("Product Page Title:", driver.title)
# driver.switch_to.window(parentWin)
btnAdd = driver.find_element(By.ID, "add-cart-button-id")
btnAdd.click()
driver.switch_to.default_content()
time.sleep(1)
driver.quit()
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(2)
main = driver.find_element(By.XPATH, "//table[@id='customers']")
rows = main.find_elements(By.TAG_NAME, "tr")
first_row = rows[1]
print(first_row.text)
print("*************************")
for row in rows:
    print(row.text)
driver.quit()
C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PythonProject4\Selenium\waits.py 
Alfreds Futterkiste Maria Anders Germany
*************************
Company Contact Country
Alfreds Futterkiste Maria Anders Germany
Centro comercial Moctezuma Francisco Chang Mexico
Ernst Handel Roland Mendel Austria
Island Trading Helen Bennett UK
Laughing Bacchus Winecellars Yoshi Tannamuri Canada
Magazzini Alimentari Riuniti Giovanni Rovelli Italy
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.iplt20.com/points-table/men/2024")
wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_element_located((By.XPATH, "//table//tbody/tr")))
rows = driver.find_elements(By.XPATH, "//table//tbody/tr")
print("MATCHES")
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) >= 7:
        team = cells[1].text.strip()
        matches = cells[2].text.strip()
        print(matches)
# for row in rows:
#     cells = row.find_elements(By.TAG_NAME, "td")
#     if len(cells) >= 7:
#         team = cells[1].text.strip()
#         matches = cells[2].text.strip()
#         points = cells[6].text.strip()
#         print(f"{team}\t{matches}\t{points}")

driver.quit()
C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PythonProject4\Selenium\waits.py 
MATCHES
KKR
SRH
RR
RCB
CSK
DC
LSG
GT
PBKS
MI
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait, Select
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.facebook.com/")
btnCreate = driver.find_element(By.XPATH, "//a[text()='Create new account']")
btnCreate.click()
year = driver.find_element(By.ID, "year")
s = Select(year)
s.select_by_index(2)
s.select_by_value("1996")
s.select_by_visible_text("1998")
# s.deselect_by_index(2)
# s.deselect_by_value("1996")
# s.deselect_by_visible_text("1998")
time.sleep(3)
driver.quit()
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.facebook.com/")
txtHighlight = driver.find_element(By.XPATH, "//h2[contains(text(),'Facebook helps')]")
driver.execute_script("arguments[0].setAttribute('style','background:yellow')",txtHighlight)
time.sleep(3)
driver.quit()
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)
txtHighlight = driver.find_element(By.XPATH, "//h2[contains(text(),'Facebook helps')]")
driver.execute_script("arguments[0].setAttribute('style','background:yellow')", txtHighlight)
time.sleep(3)
btnLogin = driver.find_element(By.NAME, "login")
color = btnLogin.value_of_css_property("background-color")
font = btnLogin.value_of_css_property("font-size")
width = btnLogin.value_of_css_property("width")
fam = btnLogin.value_of_css_property("font-family")
print("Login button styles:")
print("Background Color:", color)
print("Font Size:", font)
print("Width:", width)
print("Font Family:", fam)
driver.quit()
C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PythonProject4\Selenium\waits.py 
Login button styles:
Background Color: rgba(8, 102, 255, 1)
Font Size: 20px
Width: 332px
Font Family: Helvetica, Arial, sans-serif
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# Step 1: Open Facebook
driver.get("https://www.facebook.com/")
time.sleep(2)
# Step 2: Navigate to Redbus
driver.get("https://www.redbus.in/")
time.sleep(2)
# Step 3: Go back to Facebook
driver.back()
time.sleep(2)
# Step 4: Go forward to Redbus
driver.forward()
time.sleep(2)
# Step 5: Refresh Redbus
driver.refresh()
time.sleep(2)
# Step 6: Quit browser
driver.quit()
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)
email = driver.find_element(By.ID, "email")
email.send_keys("Vaish")
wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.NAME, "login")))  # ✅ Corrected this line
login = driver.find_element(By.NAME, "login")
login.click()
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.facebook.com/")
# FluentWait using WebDriverWait with polling and ignored exceptions
wait = WebDriverWait(driver, timeout=20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
# Wait until login button is clickable
login_button = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
login_button.click()
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# Edge-specific options
options = Options()
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # Adjust only if non-standard
# Setup Edge driver
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()
driver.get("https://www.facebook.com/")
# Fluent-style wait
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
login_button = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
login_button.click()
**************************************************************************************
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Adjust if needed
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)
driver.maximize_window()
driver.get("https://www.facebook.com/")
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
login_button = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
login_button.click()
*********************************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Adjust if needed
service = Service(ChromeDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)
driver.maximize_window()
driver.get("https://www.facebook.com/")
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
login_button = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
login_button.click()
***********************************************************************************************
Execute tests in parallel
(.venv) PS C:\Users\vwank\PycharmProjects\PytestJuly25> pip install pytest-xdist

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Adjust if needed

def test_google():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
def test_facebook():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com")
    assert "Facebook" in driver.title
    driver.quit()
def test_insta():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com")
   # assert "Facebook" in driver.title
    driver.quit()
def test_gmail():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.gmail.com")
   # assert "Facebook" in driver.title
    driver.quit()
def test_rediff():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.rediffmail.com")
   # assert "Facebook" in driver.title
    driver.quit()

(.venv) PS C:\Users\vwank\PycharmProjects\PytestJuly25> pytest .\Selenium\test_webpage_login.py -n 5
                                                                                                                                     [100%]
=============================================================== 5 passed in 33.49s ================================================================ 
(.venv) PS C:\Users\vwank\PycharmProjects\PytestJuly25>  
