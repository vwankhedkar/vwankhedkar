from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#options = Options
#options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
assert "Logged In Successfully" in driver.page_source
assert "Practice Test Automation" in driver.title
driver.quit()
*****************************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Automation with Selenium")
search_box.send_keys(Keys.RETURN)
assert "Automation" in driver.title
driver.quit()
*****************************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://practice.expandtesting.com/dropdown#google_vignette")
dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("Greece")
assert "Greece" in driver.page_source
driver.quit()
*****************************************************************************************
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://artoftesting.com/samplesiteforselenium")
driver.find_element(By.XPATH, "//input[@id='male' and @value='male']").click()
driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='Performance']").click()
result = driver.find_element(By.XPATH, "//input[@type='radio' and @value='male']").text
print("**********",result)
#assert "Male" in result
driver.quit()
*****************************************************************************************
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://artoftesting.com/samplesiteforselenium")
driver.find_element(By.XPATH, "//button[text()='Generate Alert Box']").click()
time.sleep(2)
alert = driver.switch_to.alert
text1 = alert.text
print(text1)
assert "Hi! Art Of Testing, Here!" in text1
alert.accept()
driver.quit()
*****************************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://artoftesting.com/samplesiteforselenium")
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "idOfButton")))
print("Data loaded successfully")
driver.quit()
*****************************************************************************************
    
*****************************************************************************************
    
*****************************************************************************************
    
*****************************************************************************************
    
*****************************************************************************************

test_LoginPage.py
import pytest
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import TestData

@pytest.mark.usefixtures("init_driver")
class Test_Login(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()  # Fix method name spelling here too
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title()
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

confest.py
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    browser = request.param
    if browser == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        web_driver = webdriver.Firefox(GeckoDriverManager().install())

    request.cls.driver = web_driver
    yield
    web_driver.quit()

config.py
class TestData:
    CHROME_EXECUTABLE = r"C:\Java-Selenium-Train\drivers\chromedriver.exe"
    FIREFOX_EXECUTABLE = r"C:\Java-Selenium-Train\drivers\geckodriver.exe"  # ✅ Corrected
    EDGE_EXECUTABLE = r"C:\Java-Selenium-Train\drivers\msedgedriver.exe"

    BASE_URL = "https://app.hubspot.com/login"
    USER_NAME = "naveenanimation30@gmail.com"
    PASSWORD = "Selenium@12345"
    LOGIN_PAGE_TITLE = "HubSpot Login"

