D:\pytestProject\nopCommerceApp\testCases\test_login.py

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
        else:
            assert False

    def test_login(self,setup):
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        print(act_title)
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False

D:\pytestProject\nopCommerceApp\pageObjects\LoginPage.py

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id="Email"
    textbox_password_id = "Password"
    button_login_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

D:\pytestProject\nopCommerceApp\testCases\conftest.py

from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver

Output :
======
PS D:\pytestProject\nopCommerceApp> pytest -v -s testCases/test_login.py
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0 -- C:\Python311\python.exe
cachedir: .pytest_cache
rootdir: D:\pytestProject\nopCommerceApp
collected 2 items

testCases/test_login.py::Test_001_Login::test_homePageTitle
DevTools listening on ws://127.0.0.1:55783/devtools/browser/119c6c3c-da99-41a9-9d60-665236434dd3
PASSED
testCases/test_login.py::Test_001_Login::test_login
DevTools listening on ws://127.0.0.1:55799/devtools/browser/0591485d-d805-4e14-8527-cccc8d7d5e6a
Dashboard / nopCommerce administration
PASSED

=============================================================== 2 passed in 18.26s ================================================================ 
PS D:\pytestProject\nopCommerceApp> 
