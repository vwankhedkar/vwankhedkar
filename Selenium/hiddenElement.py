from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
class HiddenElement():
    def demo_is_displayed(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10   )
        driver.maximize_window()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(elem)
        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        elem1 = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(elem1)

demoDisplayed = HiddenElement()
demoDisplayed.demo_is_displayed()

True
False
