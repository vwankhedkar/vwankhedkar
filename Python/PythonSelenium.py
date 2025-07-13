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

