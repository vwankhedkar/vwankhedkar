import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    logger=LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("**********************Test_001_Login**************************")
        self.logger.info("********************Verifying Home Page Title************************")
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login123":
            assert True
            self.driver.close()
            self.logger.info("****************Home Page Title test is Passed**********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*****************Home Page title test is failed*********************")
            assert False

    def test_login(self,setup):
        self.logger.info("**********************Verifying Login Test**************************")
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
            self.logger.info("****************Login Test is passed*******************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
