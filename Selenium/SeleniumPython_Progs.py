from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
service = Service()  # Automatically detects geckodriver if added to PATH
driver = webdriver.Firefox(service=service)
driver.get("https://www.google.com")
driver.set_window_size(200, 200)
time.sleep(2)
driver.set_window_position(300, 200)
time.sleep(2)
driver.maximize_window()
driver.quit()
**********************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Prompt for browser input
browser = input("Enter Browser : GC/FF/ME => ").strip().upper()

driver = None

if browser == "GC":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browser == "FF":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
elif browser == "ME":
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
else:
    print("Invalid browser input. Use GC (Chrome), FF (Firefox), or ME (Edge).")

if driver:
    driver.get("https://www.google.com")
    time.sleep(2)
    print("Title:", driver.title)
    print("Current URL:", driver.current_url)
    driver.maximize_window()
    time.sleep(2)
    driver.quit()
*****************************************************************************
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in")
driver.find_element(By.XPATH,"//span[contains(@id,'nav-link-accountList-nav-line-1')]").click()
print(driver.title)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("9823377023")
driver.find_element(By.XPATH,"//input[@class='a-button-input']").click()
driver.save_screenshot("selenium_training_section.png")
print("Screenshot saved")
driver.close()
*****************************************************************************

*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
