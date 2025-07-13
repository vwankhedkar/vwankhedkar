import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# Fixture for Chrome
@pytest.fixture(scope='class')
def init_chrome_driver(request):
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    request.cls.driver = driver  # Fix: Correct attribute assignment
    yield
    driver.quit()
# Fixture for Firefox
@pytest.fixture(scope='class')
def init_ff_driver(request):
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    request.cls.driver = driver
    yield
    driver.quit()
# Chrome base test class
@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass
# Chrome test class
@pytest.mark.usefixtures("init_chrome_driver")
class Test_Google_Chrome(Base_Chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title
# Firefox base test class
@pytest.mark.usefixtures("init_ff_driver")
class Base_Firefox_Test:
    pass
# Firefox test class (optional)
@pytest.mark.usefixtures("init_ff_driver")
class Test_Google_Firefox(Base_Firefox_Test):
    def test_google_title_firefox(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title
ts\PytestJuly25> pytest .\Selenium\test_fixture_google.py                                   
collected 2 items                                                                                                                                  
Selenium/test_fixture_google.py::Test_Google_Chrome::test_google_title_chrome
DevTools listening on ws://127.0.0.1:64357/devtools/browser/20cbd963-93cb-4623-b7dc-0f6e73993162
PASSED
Selenium/test_fixture_google.py::Test_Google_Firefox::test_google_title_firefox PASSED

========== 2 passed in 37.04s 
**********************************************************************************
