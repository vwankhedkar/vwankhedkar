TestNGBasics.java

package com.parameters;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class ParameterTest {
	Webdriver driver;
	
	@Test 
	@Parameters({"url","emailId"})
	public void yahooLoginTest(String url, String emailId){
		System.setproperty("webdriver.chrome.driver", "c:/downloads/chromedriver.exe");
		driver = new ChromeDriver();
		driver.get(url);
		
		driver.findElement(By.xpath("//*[@id='Login-username']")).clear();
		driver.findElement(By.xpath("//*[@id='Login-username']")).sendKeys(emailId);
		driver.findElement(By.xpath("//*[@id='Login-username']")).click();
		
	}
}
***************************************************************************************

YahooApp.xml

<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd" >

<suite name="Test Automation Suite" >
  <test name="Yahoo App Test" >
  
       <Parameter name="url" values = "https://www.yahoo.com/"/>
       <Parameter name="emailId" values = "test@yahoo.com"/>
       
    <classes>
       <class name="com.parameters.ParameterTest"/>
    </classes>
  </test>

</suite>

*******************************************************************************************
Java file

package com.parameters;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class ParameterTest {
	Webdriver driver;
	
	@Test 
	@Parameters({"env","browser","url","emailId"})
	public void yahooLoginTest(String env, String browser, String url, String emailId){
		
		if (browser.equals("chrome")) {
			System.setProperty("webdriver.chrome.driver","c:/downloads/chromedriver.exe");
			driver = new ChromeDriver();
		} else (browser.equals("Firefox")) {
				System.setproperty("webdriver.gecko.driver", "c:/downloads/gekodriver.exe");
				driver = new FireFoxDriver();
		}
		driver.get(url);
		
		driver.findElement(By.xpath("//*[@id='Login-username']")).clear();
		driver.findElement(By.xpath("//*[@id='Login-username']")).sendKeys(emailId);
		driver.findElement(By.xpath("//*[@id='Login-username']")).click();
		
	}
}

***************************************************************************************
xml file 

<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd" >

<suite name="Test Automation Suite" >
  <test name="Yahoo App Test" >
  		
  	   <Parameter name="env" values = "QA"/>
  	   <Parameter name="browser" values = "chrome"/>
       <Parameter name="url" values = "https://www.yahoo.com/"/>
       <Parameter name="emailId" values = "test@yahoo.com"/>
       
    <classes>
       <class name="com.parameters.ParameterTest"/>
    </classes>
  </test>

</suite>

	
