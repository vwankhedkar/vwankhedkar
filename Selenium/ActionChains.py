from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

opt = Options()
opt.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path=r"D:\Selenium\chromedriver.exe",options=opt)
driver.get("https://www.sbilife.co.in/")
menu = driver.find_elements_by_xpath("//div[@id='container']/div[2]/ul/li")
action = ActionChains(driver)
for item in menu[0:5]:
   action.move_to_element(item).perform()
   time.sleep(5)
action.move_to_element(menu[0]).perform()
child = driver.find_element_by_link_text("Learn About Insurance")
action.move_to_element(child).click().perform()

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

