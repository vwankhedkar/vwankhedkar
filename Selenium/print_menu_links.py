learnSelenium.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LearnSelenium:
    def __init__(self, driver):
        self.driver = driver
        self.close_button = "//button[@class='_30XB9F']"
        self.menu_items = "//div[@class='_3sdu8W emupdz']"
        self.menu_item_name = "//div[@class='_2puWtW _3a3qyb']"
        self.child_menu_item_name = "//div[@class='_3sdu8W emupdz']"

    def click_close_button(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            close_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.close_button)))
            close_button.click()
        except:
            print("Close button not found or already closed.")

    def get_all_menu_item_names(self):
        menu_items = self.driver.find_elements(By.XPATH, self.menu_items)
        print("Menu items are --> ", menu_items)
        for menu in menu_items:
            print(menu.find_element(By.XPATH, self.child_menu_item_name).text)

    def close_browser(self):
        self.driver.close()

TestChildLocator.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from learnSelenium import LearnSelenium  # Make sure the class is named correctly

class TestChildLocator:
    def test_method(self):
        # Use Service object for modern Selenium compatibility
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get('https://www.flipkart.com/')
        driver.maximize_window()

        coding = LearnSelenium(driver)
        coding.click_close_button()
        coding.get_all_menu_item_names()
        coding.close_browser()

       # driver.quit()
***********************************************************************
naukri.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.naukri.com")
driver.maximize_window()
links = driver.find_elements(By.XPATH, "//div[@class='nI-gNb-wrap']")
for link in links:
    print("Links are -->", link.text)
****************************************************************

