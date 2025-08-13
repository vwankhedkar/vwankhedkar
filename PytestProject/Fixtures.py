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
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
import os
os.environ['WDM_LOCAL'] = '1'
os.environ['WDM_CACHE'] = r'C:\Temp\webdriver'  # Any folder you have access to
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("----------Setup----------------")
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")
    yield
    print("----------TearDown----------------")
    driver.quit()
@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == 'Google'
@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == 'https://www.google.com/'
============================ test session starts =============================
collecting ... collected 2 items

Fixtures.py::test_google_title ----------Setup----------------
PASSED                                    [ 50%]
Fixtures.py::test_google_url PASSED                                      [100%]----------TearDown----------------


============================= 2 passed in 20.46s ==============================

Process finished with exit code 0
******************************************************************************************************
import os
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Set webdriver_manager cache location to avoid permission issues
os.environ['WDM_LOCAL'] = '1'
os.environ['WDM_CACHE'] = r'C:\Temp\webdriver'  # Make sure this folder exists

@pytest.fixture(scope='class')
def init_chrome_driver(request):
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    sleep(2)
    driver.quit()

@pytest.fixture(scope='class')
def init_ff_driver(request):
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    sleep(2)
    driver.quit()

@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass

class Test_Google_Chrome(Base_Chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == 'Google'

@pytest.mark.usefixtures("init_ff_driver")
class Base_Firefox_Test:
    pass

class Test_Google_Firefox(Base_Firefox_Test):
    def test_google_title_firefox(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == 'Google'
[gw0] PASSED Fixture_class.py::Test_Google_Chrome::test_google_title_chrome 
[gw1] PASSED Fixture_class.py::Test_Google_Firefox::test_google_title_firefox 

=============================================================== 2 passed in 27.00s ================================================================ 
(.venv) PS C:\Users\vwank\PycharmProjects\Python_Aug25\Pytest> pytest -v -s -n 2 .\Fixture_class.py
