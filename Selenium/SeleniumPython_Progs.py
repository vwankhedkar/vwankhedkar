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
package com.PractiseProgs;
import org.openqa.selenium.By;
import org.openqa.selenium.Point;
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.WebElement; 
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
public class openHTML { 
	public static void main(String[] args) throws InterruptedException 
	{ 
		WebDriver driver=new FirefoxDriver(); 
		driver.get("https://www.amazon.in/"); 
		RemoteWebDriver r= (RemoteWebDriver) driver; 
		WebElement ele = driver.findElement(By.linkText("Your Amazon.in"));
		System.out.println(ele);
		Point p = ele.getLocation();
		int y = p.getY();
		String s = "window.scrollTo(0,"+y+")";
		Thread.sleep(3000);
		//String c="window.scrollTo(0,document.body.scrollHeight)"; 
		r.executeScript(s);  
		driver.quit();
	}
} 
*****************************************************************************
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.edge.EdgeDriver;
	
	public class LocatorDemo2 {
	
		public static void main(String[] args)
		{
			WebDriver driver=new EdgeDriver();
			driver.get("https://automationplayground.com/crm/login.html");
			driver.findElement(By.name("email-name")).sendKeys("vikasloud@gmail.com");
			driver.findElement(By.id("password")).sendKeys("test123");
			driver.findElement(By.id("remember")).click();
			driver.findElement(By.id("submit-id")).click();
 
	
		}
*****************************************************************************
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("D:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
# //a[contains(@href,'shop')]  a[href*='shop']
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME,"alert-success").text
print(successText)
assert "Success! Thank you!" in successText
driver.close()
*************************************************************************************
Sorting dropdown
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
dropdown = Select(driver.find_element(By.XPATH, "//select[@id='animals']"))
options = dropdown.options
original_list = []
tmp_list = []
for option in options:
    original_list.append(option.text)
    tmp_list.append(option.text)
print("Before sorting ...")
print("Original List:", original_list)
print("Temp List:", tmp_list)
tmp_list.sort()
# Print both lists
print("After sorting ...")
print("Original List:", original_list)
print("Temp List:", tmp_list)
driver.quit()
*****************************************************************************
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
options = Options()
options.set_preference("dom.webnotifications.enabled", False)
service = Service()
driver = webdriver.Firefox(service=service, options=options)
try:
    driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
    select_element = driver.find_element(By.TAG_NAME, "select")
    select = Select(select_element)
    select.select_by_visible_text("India")
    print("Selected india")
finally:
    driver.quit()
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
