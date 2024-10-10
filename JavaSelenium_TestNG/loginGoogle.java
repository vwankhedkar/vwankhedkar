package com.test;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testing.annotations.AfterMethod;
import org.testing.annotations.BeforeMethod;
import org.testing.annotations.Test;

public class GoodTest {
	
	WebDriver driver;
	
	//1   //4  //7
	@BeforeMethod
	public void SetUp() {
		System.setProperty("webdriver.chrome.driver", "c:/Downloads/chromedriver");
		driver = new ChromeDriver(); // launch chrome
		driver.manage().window().maximize();
		driver.manage().deleteAllCookies();
		drive.manage().timeouts().pageLoadTimeout(40, TimeUnit.SECONDS);
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		driver.get("https://www.google.com");
	}
	
	// 2
	@Test (priority=1)
	public void googleTitleTest() {
		String title = driver.getTitle();
		System.out.println(title);	
	}
	
	// 8
	@Test (priority=2)
	public static void googleLogoTest() {
		boolean b = driver.findElement(By.xpath("//*[@id='hplogo']")).isDisplayed();
	}
	
	// 5
	@Test (priority=3)
	public void mailLickTest() {
		boolean b = driver.findElement(By.linkText("Mail")).isDisplayed();
	}
	
	//3  //6   //9
	@AfterMethod
	public void tearDown()	{
		driver.quit();
	}
}

****************************************************************************************

package com.test;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testing.annotations.AfterMethod;
import org.testing.annotations.BeforeMethod;
import org.testing.annotations.Test;

public class GoodTest {
	
	WebDriver driver;
	
	@BeforeMethod
	public void SetUp() {
		System.setProperty("webdriver.chrome.driver", "c:/Downloads/chromedriver");
		driver = new ChromeDriver(); // launch chrome
		driver.manage().window().maximize();
		driver.manage().deleteAllCookies();
		drive.manage().timeouts().pageLoadTimeout(40, TimeUnit.SECONDS);
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		driver.get("https://www.google.com");
	}
	
	@Test
	public void googleTitleTest() {
		String title = driver.getTitle();
		System.out.println(title);	
		Assert.assertEquals(title, "Google123", "title is not matched")
	}

	@AfterMethod
	public void tearDown() {
		driver.quit()
	}
}
****************************************************************************************
	package com.test;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testing.annotations.AfterMethod;
import org.testing.annotations.BeforeMethod;
import org.testing.annotations.Test;

public class GoodTest {
	
	WebDriver driver;
	
	@BeforeMethod
	public void SetUp() {
		System.setProperty("webdriver.chrome.driver", "c:/Downloads/chromedriver");
		driver = new ChromeDriver(); // launch chrome
		driver.manage().window().maximize();
		driver.manage().deleteAllCookies();
		drive.manage().timeouts().pageLoadTimeout(40, TimeUnit.SECONDS);
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		driver.get("https://www.google.com");
	}
	
	@Test
	public void googleTitleTest() {
		String title = driver.getTitle();
		System.out.println(title);	
		Assert.assertEquals(title, "Google123", "title is not matched")
	}

	@Test
	public static void googleLogoTest() {
		boolean b = driver.findElement(By.xpath("//*[@id='hplogo']")).isDisplayed();
		Assert.assertTrue(b);
	}
	
	@AfterMethod
	public void tearDown() {
		driver.quit()
	}
}

***********************************************************
TestNG.xml

<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd" >

<suite name="Test Automation Suite" >
  <test name="Different testing features test" >
    <classes>
       <class name="com.test.ExceptionTimeout" />
       <class name="com.test.GoogleTest" />
       <class name="com.test.GoogleLogoTest" />
    </classes>
  </test>

</suite>
	

